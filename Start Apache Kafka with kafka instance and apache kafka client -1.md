Title: Start Apache Kafka with kafka instance and apache kafka client -1
Date: 2017-12-23 15:15
Category: hands on
Tags: Apache kafka
Slug: Kafka Intro 
Author: Mohcine Madkour
Illustration: background.jpg

# Start Apache Kafka with kafka instance and apache kafka client

**System Architecture**
There are a bunch of processes that we need to start to run our cluster :
1. Zookeeper : Which is used by Kafka to maintain state between the nodes of the cluster.
2. Kafka brokers : The “pipes” in our pipeline, which store and emit data.
3. Producers : That insert data into the cluster.
4. Consumers : That read data from the cluster.

![Architecture](/images/basic_arch.svg)

    
## Starting Zookeeper

Zookeeper is a key value store used to maintain server state. Kafka requires a Zookeeper server in order to run, so the first thing we need to do is start a Zookeeper instance.

Inside the extracted kafka_2.11-1.0.0, you will conveniently find a bin/zookeeper-server-start.sh file (which is used to start the server), and a config/zookeeper.properties (which provides the default configuration for the zookeeper server to run)

Start the server by running (inside the kafka folders root) :

    ~/Software/kafka_2.11-1.0.0/bin/zookeeper-server-start.sh config/zookeeper.properties

You should see a confirmation that the server has started.

If you inspect the config/zookeeper.properties file, you should see the clientPort property set to 2181, which is the port that your zookeeper server is currently listening on.

##Starting our brokers

Kafka brokers form the heart of the system, and act as the pipelines where our data is stored and distributed.

Similar to how we started Zookeeper, there are two files that represent the file to start (bin/kafka-server-start.sh) and configure (config/server.properties) the broker server.

Since we would like to showcase the distributed nature of kafka, let’s start up 3 brokers, as shown in the previous diagram.

If you open the config/server.properties file, you will see a whole bunch of configuration that you, for the most part, do not have to worry about. There are, however, 3 properties, that have to be unique for each broker instance:

    broker.id=0
    listeners=PLAINTEXT://:9092
    log.dirs=/tmp/kafka-logs

Since we will have 3 servers, it’s better to maintain 3 configuration files for each server. Copy the config/server.properties file and make 3 files for each server instance:

    cp config/server.properties config/server.1.properties
    cp config/server.properties config/server.2.properties
    cp config/server.properties config/server.3.properties

Change the above 3 properties for each copy of the file so that they are all unique.

server.1.properties

    broker.id=1
    listeners=PLAINTEXT://:9093
    log.dirs=/tmp/kafka-logs1

server.2.properties

broker.id=2
listeners=PLAINTEXT://:9094
log.dirs=/tmp/kafka-logs2

server.3.properties

    broker.id=3
    listeners=PLAINTEXT://:9095
    log.dirs=/tmp/kafka-logs3

Also, create the log directories that we configured:

    mkdir /tmp/kafka-logs1
    mkdir /tmp/kafka-logs2
    mkdir /tmp/kafka-logs3

Finally, we can start the broker instances. Run the below three commands on different terminal sessions:

    bin/kafka-server-start.sh config/server.1.properties

    bin/kafka-server-start.sh config/server.2.properties

    bin/kafka-server-start.sh config/server.3.properties

You should see a startup message when the brokers start successfully, as well as logs on the Zookeeper instance that tell you of a new connection with each broker.

##Creating a topic

Before we can start putting data into your cluster, we need to create a topic to which the data will belong. To do this, run the command:

    bin/kafka-topics.sh --create --topic my-kafka-topic --zookeeper localhost:2181 --partitions 3 --replication-factor 2

The paritions options lets you decide how many brokers you want your data to be split between. Since we set up 3 brokers, we can set this option to 3.

The replication-factor describes how many copies of you data you want (in case one of the brokers goes down, you still have your data on the others).

Once you create the topic, you should see a confirmation message.
##The producer instance

The “producer” is the process that puts data into our Kafka cluster. The command line tools in the bin directory provide us with a console producer, that inputs data into the cluster every time your enter text into the console.

To start the console producer, run the command:

    bin/kafka-console-producer.sh --broker-list localhost:9093,localhost:9094,localhost:9095 --topic my-kafka-topic

The broker-list option points the producer to the addresses of the brokers that we just provisioned, and the topic option specifies the topic you want the data to come under.

You should now see a command prompt, in which you can enter a bunch of text which gets inserted into the Kafka cluster you just created every time you hit enter.
##Consumers

The only thing left to do is read data from the cluster.

Run the command:

    bin/kafka-console-consumer.sh --bootstrap-server localhost:9093 --topic my-kafka-topic --from-beginning

The bootstrap-server can be any one of the brokers in the cluster, and the topic should be the same as the topic under which you producers inserted data into the cluster.

The from-beginning option tells the cluster that you want all the messages that it currently has with it, even messages that we put into it previously.

When you run the above command, you should immediately see all the messages that you input using the producer, logged onto your console.

Additionally, if you input anymore messages with the producer while the consumer is running, you should see it output into the console in real time.

'''And in this way, Kafka acts sort of like a persistent message queue, saving the messages that were not yet read by the consumer, while passing on new messages as they come while the consumer is running'''

##Messing things up

Now that we are all done setting up and running a Kafka cluster on our system, let’s test how persistent Kafka can be.

Shut down one of the three brokers that you ran, and you should see that your cluster is still running fine. This means that Kafka is tolerant to some of its nodes failing.

Try starting another consumer in a different terminal window:

    bin/kafka-console-consumer.sh --bootstrap-server localhost:9093 --topic my-kafka-topic --from-beginning --group group2

The only thing we’ve added here is the group option, which differentiates one consumer from another. Once you start this, you should see all messages getting logged on the console from the beginning. Even though one of our brokers was shut down, our data was not lost. This is because the replication factor of 2 that we set earlier ensured that a copy of our data was present on multiple brokers.

You can play around with your setup in many more ways. What happens if you take down another broker? What if you had 5 brokers and took 2 of them down? What if you changed the replication factor for your topic?

The best way to know how resilient Kafka is, is to experiment with it yourself.