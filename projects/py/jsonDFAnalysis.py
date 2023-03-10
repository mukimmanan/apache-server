import datetime

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import re

spark = SparkSession.builder.master("local[*]") \
    .config("spark.ui.port", 6066) \
    .config("spark.sql.shuffle.partitions", 100) \
    .appName('Json RDD Analysis') \
    .getOrCreate()

schema = StructType(
    [
        StructField('authors', StringType(), True),
        StructField('categories', StringType(), True),
        StructField('license', StringType(), True),
        StructField('comments', StringType(), True),
        StructField('abstract', StringType(), True),
        StructField('version', ArrayType(StringType()), True),
    ]
)

data = spark.read.json("file:///projects/datasets/arxiv-metadata-oai-snapshot.json", schema=schema)
print("Number of records =", data.count())
data.show()
data.printSchema()

data = data.dropna(subset=['comments'])
data = data.fillna(value="Unknown", subset=["license"])
data.show()

data.createOrReplaceTempView("archive")
data = spark.sql("SELECT authors FROM archive WHERE categories LIKE 'math%'")
data.show()