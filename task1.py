
# Task 1

from data import items
import sqlite3  # SQLite databases

# open connection -- store.db
conn = sqlite3.connect("store.db")

# cursor -- run SQL command
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute("""

    CREATE TABLE products (

        product_name        CHAR(20) NOT NULL,
        price               NUMERIC(10,2) NOT NULL,
        quantity_in_stock    INTEGER NOT NULL,
        expiry_date         DATE

    )

""")


for item in items:
    # only date has none
    if item["expiry_date"] is None:
        expiry = "NULL"

    else:
        expiry = f"'{item['expiry_date']}'"

    cursor.execute(
        f"INSERT INTO products (product_name, price, quantity_in_stock, expiry_date) VALUES ('{item['product_name']}', {float(item['price'])}, {int(item['quantity_in_stock'])}, {expiry})"
    )

conn.commit()
conn.close()
