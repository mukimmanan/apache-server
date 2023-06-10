import threading

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .master("local[*]") \
    .config("spark.ui.port", "6067") \
    .config("spark.executor.cores", "8") \
    .config("spark.executor.memory", "8g") \
    .appName("Spark Practise") \
    .config("spark.scheduler.mode", "FAIR") \
    .config("spark.scheduler.allocation.file",
            "/Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/pool.xml") \
    .getOrCreate()


# def Job1():
#     spark.sparkContext.setLocalProperty("spark.scheduler.pool", "a_different_pool")
#     data = spark.read.csv(
#         "file:///Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/CompleteDataset.csv")
#     # data.count()
#     data.foreach(lambda val: print(val))
#
#
# def Job2():
#     spark.sparkContext.setLocalProperty("spark.scheduler.pool", "a_different_pool")
#     data = spark.read.csv(
#         "file:///Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/CompleteDataset.csv")
#     data.foreach(lambda val: print(val))


def Job3():
    spark.sparkContext.setLocalProperty("spark.scheduler.pool", "a_different_pool")
    data = spark.read.csv(
        "file:///Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/arxiv-metadata-oai-snapshot.json")
    data.foreach(lambda val: print(val))


def Job4():
    spark.sparkContext.setLocalProperty("spark.scheduler.pool", "fair_pool")
    data = spark.read.json(
        "file:///Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/arxiv-metadata-oai-snapshot.json")
    data.foreach(lambda val: print(val))


def Job5():
    spark.sparkContext.setLocalProperty("spark.scheduler.pool", "fair_pool")
    data = spark.read.json(
        "file:///Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/arxiv-metadata-oai-snapshot.json")
    data.foreach(lambda val: print(val))


def Job6():
    spark.sparkContext.setLocalProperty("spark.scheduler.pool", "a_different_pool")
    data = spark.read.json(
        "file:///Users/mananmukim/Desktop/Data Engineering/apache/projects/datasets/arxiv-metadata-oai-snapshot.json")
    data.foreach(lambda val: print(val))


# t1 = threading.Thread(target=Job1)
# t2 = threading.Thread(target=Job2)
t3 = threading.Thread(target=Job3)
t4 = threading.Thread(target=Job4)
t5 = threading.Thread(target=Job5)
# t6 = threading.Thread(target=Job6)

# t1.start()
# t2.start()
t3.start()
t4.start()
t5.start()
# t6.start()

# t1.join()
# t2.join()
t3.join()
t4.join()
t5.join()
# t6.join()

input()
spark.stop()
