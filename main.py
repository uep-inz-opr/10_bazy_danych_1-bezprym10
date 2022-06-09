import csv
import sqlite3


if __name__ == "__main__":
    sql_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = sql_con.cursor()
    cursor.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                    to_subscriber data_type INTEGER, 
                    datetime data_type timestamp, 
                    duration data_type INTEGER , 
                    celltower data_type INTEGER);''')

    with open(r'data\polaczenia_duze.csv', encoding='UTF-8') as fin:
        reader = csv.reader(fin, delimiter = ";")
        header = next(reader, None)
        rows = list(reader)
        cursor.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?)", rows,)
        sql_con.commit()
        result = cursor.execute("Select sum(duration) from polaczenia").fetchone()[0]
        print(int(result))
