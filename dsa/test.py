import os
from pyspark.sql import SparkSession

# Fix for Windows: point Spark to valid Python interpreter
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

# Start Spark
spark = SparkSession.builder \
    .appName("FixPython3OnWindows") \
    .master("local[*]") \
    .getOrCreate()

# Simple RDD test
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
print("RDD Output:", rdd.take(3))

spark.stop()
