from pyspark.sql import SparkSession


spark = SparkSession.builder.config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/").enableHiveSupport().appName("Learning Pyspark Airline").master("local").getOrCreate()
spark.conf.set("spark.sql.shuffle.partitions", "2")

# spark.catalog
spark.sql("DROP DATABASE IF EXISTS demo CASCADE")
spark.sql("CREATE DATABASE demo")
spark.catalog.setCurrentDatabase("demo")
print(spark.catalog.listDatabases())
print(spark.catalog.currentDatabase())

l = [('X',)]
data = spark.createDataFrame(l, schema="dummy STRING")
data.show()

# ignore, error, append, overwrite
data.write.saveAsTable("dual", mode="overwrite")
print("Tables =", spark.catalog.listTables())

spark.read.table('dual').show()
# spark.catalog.createTable("dual2", schema=data.schema)
# data.write.insertInto('dual', overwrite=True)

spark.catalog.createExternalTable(
    "table name",
    path="",
    source="csv",
    sep="\t",
    headers="true",
    inferSchema="true"
)

# For partitions

# Partitions are not recognized/visible so we need to make it visisble
# spark.sql("MSCK REPAIR TABLE <table_name>")
# OR
# spark.catalog.recoverPartitions("table_name")
# data.write.partitionBy('col name').save()
# data.write.saveAStABLE('', mode='', paritionsBy='')

# data.createOrReplaceTempView("orders")