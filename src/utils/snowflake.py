import snowflake.connector
import os

def create_snowflake_connection():
    """
    Create a Snowflake connection using environment variables.
    """

    # Access environment variables
    snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
    snowflake_user = os.getenv("SNOWFLAKE_USER")
    snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
    snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
    snowflake_schema = os.getenv("SNOWFLAKE_SCHEMA")
    
    # Establish connection
    conn = snowflake.connector.connect(
        account=snowflake_account,
        user=snowflake_user,
        password=snowflake_password,
        database=snowflake_database,
        schema=snowflake_schema
    )
    return conn

def execute_query(conn, sql_filename):
    """
    Execute a SQL query using the Snowflake connection.
    """
    with open(sql_filename, "r") as file:
        query = file.read()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

