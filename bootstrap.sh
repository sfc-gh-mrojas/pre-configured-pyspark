pip install pyspark==3.5.3 snowflake-cli ./snowpark_connect-0.6.0-py3-none-any.whl

# Create ~/.snowflake directory if it doesn't exist
mkdir -p ~/.snowflake

# Create connections.toml file with the specified content
cat > ~/.snowflake/connections.toml << 'EOF'
default_connection_name = "spark-connect"
[spark-connect]
host="sfctest0.snowflakecomputing.com"
account="sfctest0"
user="test_spc"
password="&&&&&&&&"
warehouse="testwh_spc"
database="testdb_spc"
schema="public"
EOF

echo "Snowflake connections.toml file has been created successfully."