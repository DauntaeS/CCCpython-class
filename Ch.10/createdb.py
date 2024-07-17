import sqlite3


def main():
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE Customer (Name TEXT, Email TEXT, Sales_amount INTEGER)"""
    )

    conn.commit()
    conn.close()


main()
