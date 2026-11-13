
## Task 2 -- read adnd update
import sqlite3

conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# 1. item wiht stock < 10
print("Item with stock less than 10")
cursor.execute(
    "SELECT product_name, price, quantity_in_stock, expiry_date FROM products WHERE quantity_in_stock < 10"
)

# for row in cursor.fetchall():
#     print(row[0], row[1], row[2], row[3])

# header
print(f"{'Name':<20} {'Price':>8} {'Stock':>6} {'Expiry':>12}")
print("-" * 49)

for row in cursor.fetchall():
    print(f"{row[0]:<20} {row[1]:>8.2f} {row[2]:>6} {str(row[3]):>12}")
