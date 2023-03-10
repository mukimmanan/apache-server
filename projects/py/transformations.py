from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, concat, lpad, concat, to_date, date_format
from pyspark.sql.functions import count, countDistinct

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/").enableHiveSupport().appName("Learning Pyspark Airline").master("local").getOrCreate()

# Creating dataframe
airlines = spark.read.parquet(
    "hdfs://namenode:9000/user/spark/datasets/airtrafficdata/airtraffic_all/airtraffic-part/flightmonth=200801/",
    header=True,
    inferSchema=True,
)

schema = airlines.schema

airlines.printSchema()
print("Total Records =", airlines.count())
print("Total Distinct Rows =", airlines.distinct().count())
airlines.show(10)

# Filtering
# airlines.filter(
#     col("IsArrDelayed") == 'NO'
# ).show()

# airlines.filter(
#     airlines['Cancelled'] == 1
# ).count()

airlines.filter(
    'Cancelled = 1'
).show()

airlines.filter(
    airlines.Cancelled == 1
).show() 

############################################################
airlines.select("Year", "Month", "DayofMonth").distinct().show(31)
print("Num Days =", airlines.select("Year", "Month", "DayofMonth").distinct().count())

airlines.withColumn(
    "FlightDate",
    concat(
        col("Year"),
        lpad(col("Month"), 2, "0"),
        lpad(col("DayOfMonth"), 2, "0")
    )
).withColumn("Day", date_format(to_date(col("FlightDate"), "yyyyMMdd"), "EEEE")
).filter(
    (col("IsDepDelayed") == "YES") & (col("Day") == "Sunday")
).show()

# airlines.filter(col("").isin(['']))
# airlines.filter(col("").like(''))
# ~ For not
# airlines.filter(col("").between('', ''))
# describe/summary function to get mix, max, count, sdev

airlines.select(
    count(lit(1)).alias("Num Rows")
).show()

airlines.select(
    countDistinct("Year", "Month", "DayOfMonth").alias("Count Distinct")
).show()

# groupby/rollup/cube
airlines.groupBy(
    concat(
        col("Year"),
        lpad(col("Month"), 2, "0"),
        lpad(col("DayOfMonth"), 2, "0")
    ).alias("FlightDate")
).count().show()

airlines.groupBy(
    concat(
        col("Year"),
        lpad(col("Month"), 2, "0"),
        lpad(col("DayOfMonth"), 2, "0")
    ).alias("FlightDate")
).agg(
    count(lit(1)).alias("FlightCount"),
)

airlines.rollup(
    concat(
        col("Year"),
        lpad(col("Month"), 2, "0"),
        lpad(col("DayOfMonth"), 2, "0")
    ).alias("FlightDate")
).agg(
    count(lit(1)).alias("FlightCount"),
).show()


## When/otherwise
# spark.conf.set(spark.sql.shyffle.partitions ,2);
# col().asc_null_last