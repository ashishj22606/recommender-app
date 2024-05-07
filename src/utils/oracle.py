import cx_Oracle
import os

def create_oracle_connection():
    """
    Create an Oracle database connection using environment variables.
    """
    # Load environment variables
    oracle_user = os.environ.get("ORACLE_USER")
    oracle_password = os.environ.get("ORACLE_PASSWORD")
    oracle_dsn = os.environ.get("ORACLE_DSN")  # DSN format: host:port/service_name
    
    # Establish connection
    conn = cx_Oracle.connect(user=oracle_user, password=oracle_password, dsn=oracle_dsn)
    return conn

def execute_query(conn, sql_filename):
    """
    Execute a SQL query using the Oracle database connection.
    """
    with open(sql_filename, "r") as file:
        query = file.read()
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
