from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]") \
    .config("spark.ui.port", 6067) \
    .config("spark.sql.shuffle.partitions", 100) \
    .appName('Log file RDD Analysis') \
    .getOrCreate()

rdd = spark.read.text("../datasets/ghtorrent-logs.txt.gz").rdd.flatMap(list)
rdd = rdd.repartition(numPartitions=50)

print("Number of records =", rdd.count())
print("Printing 20 Sample Records")
print(rdd.takeSample(False, 20, 1234))

transaction_or_repo = rdd.filter(lambda x: "Repo" in x and "transaction" in x.lower())
print("Num records with Repo or Transaction info ->", transaction_or_repo.count())

web_link = rdd.filter(lambda x: "WARN" in x and "URL" in x)
print("Num records with web link with status WARN ->", web_link.count())

