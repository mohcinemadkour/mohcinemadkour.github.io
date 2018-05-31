Title: Install and cofigure Spark, Kafka, Cassandra, Zookeper
Date: 2017-01-12 16:00
Category: Real Time
Tags: Apache
Slug: Apache 
Author: Mohcine Madkour
Illustration: valuation.jpg

#Anaconda 

    export PATH="/home/mohcine/anaconda2/bin:$PATH"

#Spark:

    function snotebook ()
    {
    SPARK_PATH=/home/mohcine/Sofwares/spark-2.2.0-bin-hadoop2.7
    export PYSPARK_DRIVER_PYTHON="jupyter"
    export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
    $SPARK_PATH/bin/pyspark --master local[2]
    }


#Zookeper:

    sudo apt-get install zookeeperd,   
    Check if it is running
    netstat -ant | grep :2181

#Kafka:

download kafka on the location : /opt

    Start server: 
    sudo  /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties

Start the Kafka server as a background process:

    sudo  /opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties  /tmp/kafka.log 2>&1 &

Testing server

    sudo /opt/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing

Ask Zookeeper to list available topics on Apache Kafka

    sudo /opt/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181

Publish a sample messages to Apache Kafka topic called testing by using the following producer command

    sudo /opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testing

Use consumer command to check for messages on Apache Kafka Topic called testing

    sudo /opt/kafka/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic testing --from-beginning

#Cassandra: 

    export CASSANDRA_HOME=/opt/apache-cassandra-3.11.1
    export PATH=$CASSANDRA_HOME/bin:$PATH
        >cd $CASSANDRA_HOME/bin
        >casandra
        >cqlsh



