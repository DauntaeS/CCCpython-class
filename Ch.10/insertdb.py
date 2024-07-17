import sqlite3


def main():
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()

    cur.execute(
        """INSERT INTO Customer (Name, Email, Sales_amount)
    VALUES ("John Doe", "john.doe@example.com", 1000)"""
    )

    cur.execute(
        """INSERT INTO Customer (Name, Email, Sales_amount)
    VALUES ("Jane Smith", "jane.smith@example.com", 2000)"""
    )

    cur.execute(
        """INSERT INTO Customer (Name, Email, Sales_amount)
    VALUES ("Fon Due", "fon.due@example.com", 3000)"""
    )

    conn.commit()
    conn.close()


main()
