import datetime

from pyspark.sql import SparkSession
import json
import re

spark = SparkSession.builder.master("local[*]") \
    .config("spark.ui.port", 6066) \
    .config("spark.sql.shuffle.partitions", 100) \
    .appName('Json RDD Analysis') \
    .getOrCreate()

data = spark.read.text("file:///projects/datasets/arxiv-metadata-oai-snapshot.json").rdd.flatMap(list)
data = data.repartition(100)
data.take(1)
json_data = data.map(lambda x: json.loads(x))

print("Number of Rows =", json_data.count())
print("Total Partitions =", json_data.getNumPartitions())

print("########## Getting the first 2 records ##########")
print(json_data.take(2))

print("########## Getting all the attributes ##########")
attributes = json_data.flatMap(lambda x: x.keys()).distinct().collect()
print(attributes)

print("########## Getting the name of the licenses ##########")
licenses = json_data.map(lambda x: x["license"] if x is not None else None).distinct().collect()
print("Licenses =", licenses)

print("########## Getting shortest and longest title ##########")
largest = json_data.map(lambda x: x["title"]).reduce(lambda x, y: x if x > y else y)
shortest = json_data.map(lambda x: x["title"]).reduce(lambda x, y: x if x < y else y)
print("Max Title =", largest)
print("Short Title =", shortest)


def get_abbr(line):
    result = re.search(pattern=r"\(([A-Za-z][^_/\\<>]{5,})\)", string=line)
    if result:
        return result.group(1)


print("########## Getting Abbreviation ##########")
abbr = json_data.filter(lambda x: get_abbr(x["abstract"])).count()
print("Number of abbreviations =", abbr)


def extract_month(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").month


print("########## Getting Archive Month ##########")
month_records = json_data.map(lambda x: (extract_month(x["update_date"]), 1)).reduceByKey(lambda x, y: x + y).collect()
print(month_records)



