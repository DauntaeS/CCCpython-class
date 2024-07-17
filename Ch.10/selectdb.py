import sqlite3


def main():
    conn = sqlite3.connect("customers.db")
    cur = conn.cursor()

    cur.execute("""SELECT * FROM Customer""")
    all_results = cur.fetchall()
    print("All customers\n", all_results)
    print()

    cur.execute("""SELECT * FROM Customer WHERE Sales_amount > 1000""")
    over1k = cur.fetchall()

    print("Customers with sales greater than 1000\n")
    for val in over1k:
        print(f"{val[0]:5} {val[2]:5}")
    print()

    user = int(input("Enter the minimum sales: "))
    cur.execute(f"""SELECT * FROM Customer WHERE Sales_amount > {user}""")
    user_request = cur.fetchall()

    for row in user_request:
        print(f"{row[0]:5} {row[2]:5}")

    conn.commit()
    conn.close()


main()
