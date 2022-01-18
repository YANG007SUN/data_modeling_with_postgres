import psycopg2
from sql_queries import create_table_queries, drop_table_queries
from config import user, password

def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """

    # connect to default database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=udacity user={user} password={password}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # kill existing database
    kill_db(cur,'sparkifydb')
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect(f"host=127.0.0.1 dbname=sparkifydb user={user} password={password}")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def kill_db(cur,db_name):
    """
    kills the connection to existing database and drop the database in order
    to create a new db
    """
    cur.execute(f"""
    
    SELECT 
    pg_terminate_backend(pid) 
    FROM 
        pg_stat_activity 
    WHERE 
        pid <> pg_backend_pid()
        AND datname = '{db_name}';
    """)

def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    
    cur, conn = create_database()
    
#     drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()