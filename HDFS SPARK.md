Title: SPARK AND HDFS storage : building application from Python
Date: 2017-12-29 11:50
Category: SPARK, HDFS
Tags: HDFS, Spark
Slug: Spark HDFS Guide 
Author: Mohcine Madkour
Illustration: background.jpg

# Install HDFS



PySpark can create distributed datasets from any storage source supported by Hadoop, including your local file system, HDFS, Cassandra, HBase, Amazon S3, etc. Spark supports text files, SequenceFiles, and any other Hadoop InputFormat.

readlink -f $(which java) to check the path to java install
I ended up adding the following in ~/.bashrc:

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

export HADOOP_INSTALL=/home/mohcine/Sofwares/hadoop-3.0.0

export PATH=$PATH:$HADOOP_INSTALL/bin

PySpark can create distributed datasets from any storage source supported by Hadoop, including your local file system, HDFS, Cassandra, HBase, Amazon S3, etc. Spark supports text files, SequenceFiles, and any other Hadoop InputFormat.

# Getting started

These examples give a quick overview of the Spark API. Spark is built on the concept of distributed datasets, which contain arbitrary Java or Python objects. You create a dataset from external data, then apply parallel operations to it. The building block of the Spark API is its RDD API. In the RDD API, there are two types of operations: transformations, which define a new dataset based on previous ones, and actions, which kick off a job to execute on a cluster. On top of Spark’s RDD API, high level APIs are provided, e.g. DataFrame API and Machine Learning API. These high level APIs provide a concise way to conduct certain data operations. In this page, we will show examples using RDD API as well as examples using high level APIs.