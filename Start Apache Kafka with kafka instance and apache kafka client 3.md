Title: Start Apache Kafka with kafka instance and apache kafka client
Date: 2017-12-26 11:50
Category: Kafka, Spark Streaming
Tags: kafka, Spark
Slug: Spark Streaming + Kafka Integration Guide 
Author: Mohcine Madkour
Illustration: background.jpg


#Spark Streaming + Kafka Integration Guide for python

In this post I shed some light on the current state of Kafka integration in Spark Streaming AND how to configure Spark Streaming to receive data from Kafka. All this with the disclaimer that this happens to be my first experiment with Spark Streaming.

First of all, Spark Streaming is a sub-project of Apache Spark. Spark is a batch processing platform similar to Apache Hadoop, and Spark Streaming is a real-time processing tool that runs on top of the Spark engine.


 There are two approaches to this - the old approach using Receivers and Kafka’s high-level API, and a new approach (introduced in Spark 1.3) without using Receivers. They have different programming models, performance characteristics, and semantics guarantees. Both approaches are considered stable APIs as of the current version of Spark (2.11-1.0.0).

##Approach 1: Receiver-based Approach

This approach uses a Receiver to receive the data. The Receiver is implemented using the Kafka high-level consumer API. As with all receivers, the data received from Kafka through a Receiver is stored in Spark executors, and then jobs launched by Spark Streaming processes the data.

However, under default configuration, this approach can lose data under failures (see receiver reliability. To ensure zero-data loss, you have to additionally enable Write Ahead Logs in Spark Streaming (introduced in Spark 1.2). This synchronously saves all the received Kafka data into write ahead logs on a distributed file system (e.g HDFS), so that all the data can be recovered on failure. See Deploying section in the streaming programming guide for more details on Write Ahead Logs.

To use this approach in your streaming application,  First, In the streaming application code, import KafkaUtils and create an input DStream as follows.

    from pyspark.streaming.kafka import KafkaUtils

    kafkaStream = KafkaUtils.createStream(streamingContext, \
     [ZK quorum], [consumer group id], [per-topic number of Kafka partitions to consume])
By default, the Python API will decode Kafka data as UTF8 encoded strings. You can specify your custom decoding function to decode the byte arrays in Kafka records to any arbitrary data type as in this example


    """
     Counts words in UTF8 encoded, '\n' delimited text received from the network every second.
     Usage: kafka_wordcount.py <zk> <topic>
     To run this on your local machine, you need to setup Kafka and create a producer first, see
     http://kafka.apache.org/documentation.html#quickstart
     and then run the example
        `$ bin/spark-submit --jars \
          external/kafka-assembly/target/scala-*/spark-streaming-kafka-assembly-*.jar \
          examples/src/main/python/streaming/kafka_wordcount.py \
          localhost:2181 test`
    """
    from __future__ import print_function
    import sys
    from pyspark import SparkContext
    from pyspark.streaming import StreamingContext
    from pyspark.streaming.kafka import KafkaUtils
    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: kafka_wordcount.py <zk> <topic>", file=sys.stderr)
            exit(-1)
        sc = SparkContext(appName="PythonStreamingKafkaWordCount")
        ssc = StreamingContext(sc, 1)
        zkQuorum, topic = sys.argv[1:]
        kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
        lines = kvs.map(lambda x: x[1])
        counts = lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a+b)
        counts.pprint()
        ssc.start()
    ssc.awaitTermination()

Deploying :  Run on terminal:

    spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 /home/mohcine/Spark_Streaming_kafka.py localhost:2182

##Approach 2: Direct Approach (No Receivers)

This new receiver-less “direct” approach has been introduced in Spark 1.3 to ensure stronger end-to-end guarantees. Instead of using receivers to receive data, this approach periodically queries Kafka for the latest offsets in each topic+partition, and accordingly defines the offset ranges to process in each batch. When the jobs to process the data are launched, Kafka’s simple consumer API is used to read the defined ranges of offsets from Kafka (similar to read files from a file system). Note that this feature was introduced in Spark 1.3 for the Scala and Java API, in Spark 1.4 for the Python API.

This approach has the following advantages over the receiver-based approach (i.e. Approach 1).

- Simplified Parallelism: No need to create multiple input Kafka streams and union them. With directStream, Spark Streaming will create as many RDD partitions as there are Kafka partitions to consume, which will all read data from Kafka in parallel. So there is a one-to-one mapping between Kafka and RDD partitions, which is easier to understand and tune.

- Efficiency: Achieving zero-data loss in the first approach required the data to be stored in a Write Ahead Log, which further replicated the data. This is actually inefficient as the data effectively gets replicated twice - once by Kafka, and a second time by the Write Ahead Log. This second approach eliminates the problem as there is no receiver, and hence no need for Write Ahead Logs. As long as you have sufficient Kafka retention, messages can be recovered from Kafka.

- Exactly-once semantics: The first approach uses Kafka’s high level API to store consumed offsets in Zookeeper. This is traditionally the way to consume data from Kafka. While this approach (in combination with write ahead logs) can ensure zero data loss (i.e. at-least once semantics), there is a small chance some records may get consumed twice under some failures. This occurs because of inconsistencies between data reliably received by Spark Streaming and offsets tracked by Zookeeper. Hence, in this second approach, we use simple Kafka API that does not use Zookeeper. Offsets are tracked by Spark Streaming within its checkpoints. This eliminates inconsistencies between Spark Streaming and Zookeeper/Kafka, and so each record is received by Spark Streaming effectively exactly once despite failures. In order to achieve exactly-once semantics for output of your results, your output operation that saves the data to an external data store must be either idempotent, or an atomic transaction that saves results and offsets (see Semantics of output operations in the main programming guide for further information).

Note that one disadvantage of this approach is that it does not update offsets in Zookeeper, hence Zookeeper-based Kafka monitoring tools will not show progress. However, you can access the offsets processed by this approach in each batch and update Zookeeper yourself (see below).

Next, we discuss how to use this approach in your streaming application.
In the streaming application code, import KafkaUtils and create an input DStream as follows.

    from pyspark.streaming.kafka import KafkaUtils
    directKafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})

You can also pass a messageHandler to createDirectStream to access KafkaMessageAndMetadata that contains metadata about the current message and transform it to any desired type. By default, the Python API will decode Kafka data as UTF8 encoded strings. You can specify your custom decoding function to decode the byte arrays in Kafka records to any arbitrary data type. See the following example:


    """
     Counts words in UTF8 encoded, '\n' delimited text directly received from Kafka in every 2 seconds.
     Usage: direct_kafka_wordcount.py <broker_list> <topic>
     To run this on your local machine, you need to setup Kafka and create a producer first, see
     http://kafka.apache.org/documentation.html#quickstart
     and then run the example
        `$ bin/spark-submit --jars \
          external/kafka-assembly/target/scala-*/spark-streaming-kafka-assembly-*.jar \
          examples/src/main/python/streaming/direct_kafka_wordcount.py \
          localhost:9092 test`
    """
    from __future__ import print_function
    import sys
    from pyspark import SparkContext
    from pyspark.streaming import StreamingContext
    from pyspark.streaming.kafka import KafkaUtils
    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: direct_kafka_wordcount.py <broker_list> <topic>", file=sys.stderr)
            exit(-1)
        sc = SparkContext(appName="PythonStreamingDirectKafkaWordCount")
        ssc = StreamingContext(sc, 2)
        brokers, topic = sys.argv[1:]
        kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
        lines = kvs.map(lambda x: x[1])
        counts = lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a+b)
        counts.pprint()
        ssc.start()
    ssc.awaitTermination()

In the Kafka parameters, you must specify either metadata.broker.list or bootstrap.servers. By default, it will start consuming from the latest offset of each Kafka partition. If you set configuration auto.offset.reset in Kafka parameters to smallest, then it will start consuming from the smallest offset.

You can also start consuming from any arbitrary offset using other variations of KafkaUtils.createDirectStream. Furthermore, if you want to access the Kafka offsets consumed in each batch, you can do the following.

    offsetRanges = []
    def storeOffsetRanges(rdd):
    global offsetRanges
    offsetRanges = rdd.offsetRanges()
    return rdd
    def printOffsetRanges(rdd):
    for o in offsetRanges:
         print "%s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset)
    directKafkaStream \
     .transform(storeOffsetRanges) \
     .foreachRDD(printOffsetRanges)

You can use this to update Zookeeper yourself if you want Zookeeper-based Kafka monitoring tools to show progress of the streaming application.

Note that the typecast to HasOffsetRanges will only succeed if it is done in the first method called on the directKafkaStream, not later down a chain of methods. You can use transform() instead of foreachRDD() as your first method call in order to access offsets, then call further Spark methods. However, be aware that the one-to-one mapping between RDD partition and Kafka partition does not remain after any methods that shuffle or repartition, e.g. reduceByKey() or window().

Another thing to note is that since this approach does not use Receivers, the standard receiver-related (that is, configurations of the form spark.streaming.receiver.* ) will not apply to the input DStreams created by this approach (will apply to other input DStreams though). Instead, use the configurations spark.streaming.kafka.*. An important one is spark.streaming.kafka.maxRatePerPartition which is the maximum rate (in messages per second) at which each Kafka partition will be read by this direct API.