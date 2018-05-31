Title: Start Apache Spark : building application from Python
Date: 2017-12-29 11:50
Category: Kafka, Spark Streaming
Tags: Spark
Slug: Spark Guide 
Author: Mohcine Madkour
Illustration: background.jpg
# Converting Python to Spark

1. You can't do I/Os the old fashion way; whatever dataset you're manipulating must be distributed; ie your log file should be on HDFS. So first step, opening the log file and creating a RDD would look something like this:
>> Spark put files in HDFS
>> 



2. You don't programmatically iterate on the data per say, instead you supply a function to process each value (lines in this case). So your code where you iterate on lines could be put inside a function:


    def virtualPortFunction(line):
        #Do something, return output process of a line
        virtualPortsSomething = lines.flatMap(lambda x: x.split(' ')) \
                     .map(lambda x: virtualPortFunction(x))

                     