import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
    except Error as e:
        print(f"Error connection to {db_file} - {e}")
    return conn


def execute_query(conn, query):
    """
    Execute query against the db
    :param conn: the Connection object
    :param query: the query to execute
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
    except sqlite3.OperationalError as oe:
        print(f"Invalid query - {query}")
        results = oe
    return results


def main():
    database = r"../reader.db"
    conn = create_connection(database)
    with conn:
        query = "SELECT id FROM bib;"
        res = execute_query(conn, query)
        print(res)


if __name__ == '__main__':
    main()
