import datetime

from pyspark.sql import SparkSession
from pprint import pprint
import json
import re

spark = SparkSession.builder.master("local[*]") \
    .config("spark.ui.port", 6067) \
    .config("spark.sql.shuffle.partitions", 100) \
    .appName('KDD RDD Analysis') \
    .getOrCreate()

rdd = spark.read.text("../datasets/kddcup.data.gz").rdd.flatMap(list)
rdd = rdd.repartition(numPartitions=10)

pprint(rdd.takeSample(False, 10, 23))