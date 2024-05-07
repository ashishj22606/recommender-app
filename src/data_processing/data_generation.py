from src.utils import oracle, snowflake

def generate_data_oracle():
    # Create Oracle connection
    conn = oracle.create_oracle_connection()

    # Execute SQL query for data generation
    sql_filename = "sql/data_generation_query_oracle.sql"
    result = oracle.execute_query(conn, sql_filename)

    # Process query results (if needed)
    # For example, write data to files or perform additional processing
    print("Data generation from Oracle completed.")

def generate_data_snowflake():
    # Create Snowflake connection
    conn = snowflake.create_snowflake_connection()

    # Execute SQL query for data generation
    sql_filename = "sql/data_generation_query_snowflake.sql"
    result = snowflake.execute_query(conn, sql_filename)

    # Process query results (if needed)
    # For example, write data to files or perform additional processing
    print("Data generation from Snowflake completed.")
