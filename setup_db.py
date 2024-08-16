import mysql.connector
from mysql.connector import errorcode
import argparse

def create_tables(db_config):
    TABLES = {}
    TABLES['Event'] = (
        "CREATE TABLE IF NOT EXISTS Event ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  univoc_id VARCHAR(255) NOT NULL,"
        "  name VARCHAR(255) NOT NULL,"
        "  description TEXT NOT NULL,"
        "  date_start DATE NOT NULL,"
        "  date_and DATE NOT NULL,"
        "  do TINYINT(1) NOT NULL DEFAULT 1,"
        "  repeat_event TINYINT(1) NOT NULL DEFAULT 0,"
        "  calendar TEXT NOT NULL"
        ") ENGINE=InnoDB"
    )

    TABLES['Diary'] = (
        "CREATE TABLE IF NOT EXISTS Diary ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  id_diary VARCHAR(255) NOT NULL,"
        "  Name VARCHAR(255) NOT NULL,"
        "  data_creation DATE NOT NULL"
        ") ENGINE=InnoDB"
    )

    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print(f"Creating table {table_name}: ", end='')
                cursor.execute(table_description)
                print("OK")
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("Table already exists.")
                else:
                    print(err.msg)
            else:
                print(f"Table {table_name} created successfully.")

        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    else:
        cnx.close()

def main():
    parser = argparse.ArgumentParser(description="Create tables in MySQL database.")
    parser.add_argument('--user', required=True, help="Database user")
    parser.add_argument('--password', required=True, help="Database password")
    parser.add_argument('--host', default='localhost', help="Database host")
    parser.add_argument('--database', required=True, help="Database name")

    args = parser.parse_args()

    db_config = {
        'user': args.user,
        'password': args.password,
        'host': args.host,
        'database': args.database
    }

    create_tables(db_config)

if __name__ == "__main__":
    main()
