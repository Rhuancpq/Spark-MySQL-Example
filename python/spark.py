from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.config("spark.jars", "./jdbc/mysql-connector-java-8.0.24.jar") \
    .master("spark://spark:7077").appName("PySpark_MySQL_ETL_example").getOrCreate()


# EXTRACT
emps = spark.read.format("jdbc").option("url", "jdbc:mysql://mysql:3306/employees") \
    .option("driver", "com.mysql.cj.jdbc.Driver").option("dbtable", "EMPLOYEES") \
    .option("user", "root").option("password", "root123").load()

# TRANSFORM
emps_90s = emps.filter(col('hire_date').between('1990-1-1', '1999-12-31'))

emps_90s.show()

# LOAD 
# Wherever you want