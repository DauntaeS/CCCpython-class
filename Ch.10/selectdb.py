import sqlite3


def main():
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()

    user_request = int(input("Enter the minimum sales: "))

    # cur.execute("""SELECT * FROM Customer""")
    # cur.execute("""SELECT * FROM Customer WHERE Sales_amount > 1000""")
    cur.execute(f"""SELECT * FROM Customer WHERE Sales_amount > {user_request}""")

    results = cur.fetchall()

    for row in results:
        print(f"{row[0]:5} {row[2]:5}")

    conn.commit()
    conn.close()


main()
