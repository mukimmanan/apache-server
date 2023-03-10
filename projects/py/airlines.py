from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, IntegerType, StructType, NumericType
from pyspark.sql.functions import col, lit, concat


spark = SparkSession.builder.appName("Learning Pyspark Airline").config("deployment.mode", "client").master("yarn").getOrCreate()

# Creating dataframe
# airlines = spark.read.csv(
#     "hdfs://namenode:9000/user/spark/datasets/airtrafficdata/airlines_all/airlines",
#     header=True,
#     inferSchema=True
# )

# schema = airlines.schema

# airlines.printSchema()
# print("Total Records =", airlines.count())
# print("Total Distinct Rows =", airlines.distinct().count())
# airlines.show(10)

employees = [
    (1, "Scott", "Tiger", 1000.0, "united states"),
    (2, "Henry", "Ford", 1250.0, "India"),
    (3, "Nick", "Junior", 750.0, "united KINGDOM"),
    (4, "Bill", "Gomes", 1500.0, "AUSTRALIA")
]

employees = spark.createDataFrame(
    employees, schema="""
        employee_id INT,
        first_name STRING,
        last_name STRING,
        salary FLOAT,
        nationality STRING
    """
)

employees.printSchema()
employees.show()

# Projection
employees.select("first_name", "last_name").show()
employees.drop("nationality")
employees.withColumn("full_name", concat('first_name', lit(' '), 'last_name')).show()
employees.selectExpr("concat(first_name, ' ', last_name) AS full_name").show()
employees.select("employee_id", concat("first_name", lit(' '), "last_name").alias("full_name")).show()

# employees.write.parquet("", mode="overwrite", compression=None)
# employees.write.mode("overwrite").option("compression", 'none').format('parquet').save("")
# employees.write.mode('overwrite').option('compression', 'none').parquet("")
# employees.coalesce(1).write.mode('overwrite').option('compression', 'none').parquet("")
# employees.coalesce(1).write.mode('ignore').option('compression', 'none').parquet("") # For ignoring write if path already present

# when-otherwise 