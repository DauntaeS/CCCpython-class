import sqlite3


def main():
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE Customer (Customer_id INTEGER, Name TEXT, Email TEXT, Sales_amount REAL)"""
    )

    cur.execute(
        """INSERT INTO Customer (Customer_id, Name, Email, Sales_amount)
    VALUES (1, "John Doe", "john.doe@example.com", 1000)"""
    )

    cur.execute(
        """INSERT INTO Customer (Customer_id, Name, Email, Sales_amount)
    VALUES (2, "Jane Smith", "jane.smith@example.com", 2000)"""
    )

    cur.execute(
        """INSERT INTO Customer (Customer_id, Name, Email, Sales_amount)
    VALUES (3, "Fon Due", "fon.due@example.com", 3000)"""
    )

    print("Database created and data inserted successfully")
    print()

    cur.execute("""SELECT * FROM Customer""")
    all_results = cur.fetchall()
    print("All customers\n", all_results)
    print()

    cur.execute("""SELECT * FROM Customer WHERE Sales_amount > 1000""")
    over1k = cur.fetchall()

    print("Customers with sales greater than 1000\n")
    for val in over1k:
        print(f"{val[1]:5} {val[3]:5}")
    print()

    user = float(input("Enter the minimum sales: "))
    print(f"Customers with sales greater than {user}")

    cur.execute(f"""SELECT * FROM Customer WHERE Sales_amount > {user}""")
    user_request = cur.fetchall()

    for row in user_request:
        print(f"{row[1]:5} {row[3]:5}")

    conn.commit()
    conn.close()


main()
