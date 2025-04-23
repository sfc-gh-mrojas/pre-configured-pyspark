from pyspark.sql import SparkSession
from pyspark.sql.functions import col

import os
from snowflake import snowpark_connect
snowpark_connect.start_session(remote_url=os.environ["SPARK_REMOTE"]) 

# Create SparkSession
spark = SparkSession.builder \
    .appName("Spark Connect Example") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 29),
    ("Bob", 31),
    ("Catherine", 25)
]

# Create DataFrame with column names
df = spark.createDataFrame(data, ["name", "age"])
df.show()

# Apply transformation: filter age > 28 and add "age_in_5_years"
transformed_df = df.filter(col("age") > 28) \
                   .withColumn("age_in_5_years", col("age") + 5)

transformed_df.show()

# Write to a table (will write to default Spark catalog unless you're using Spark Connect to Snowflake)
transformed_df.write.mode("overwrite").saveAsTable("client_app_people_transformed")

# Read the table back
table_df = spark.table("client_app_people_transformed")
table_df.show()

# Read Snowflake table (if using Spark + Snowflake connector)
# NOTE: Requires proper Snowflake connector configs set
snowflake_table_df = spark.table("SAMPLE_DATA.TPCH_SF1.CUSTOMER")
snowflake_table_df.show()

# Stop session
spark.stop()
