
import sqlite3
import json

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

# Drop tables if they exist
cur.execute("DROP TABLE IF EXISTS order_items")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("DROP TABLE IF EXISTS customers")

# Create tables
cur.executescript("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    timestamp INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE order_items (
    order_id INTEGER,
    item_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (item_id) REFERENCES items (id)
);
""")

# Load data from JSON
with open('example_orders.json') as f:
    orders_data = json.load(f)

for order in orders_data:
    name, phone = order['name'], order['phone']
    cur.execute("INSERT OR IGNORE INTO customers (name, phone) VALUES (?, ?)", (name, phone))
    customer_id = cur.execute("SELECT id FROM customers WHERE phone = ?", (phone,)).fetchone()[0]
    cur.execute("INSERT INTO orders (customer_id, timestamp, notes) VALUES (?, ?, ?)",
                (customer_id, order['timestamp'], order.get('notes', '')))
    order_id = cur.lastrowid

    for item in order['items']:
        item_name, price = item['name'], item['price']
        cur.execute("INSERT OR IGNORE INTO items (name, price) VALUES (?, ?)", (item_name, price))
        item_id = cur.execute("SELECT id FROM items WHERE name = ?", (item_name,)).fetchone()[0]
        cur.execute("INSERT INTO order_items (order_id, item_id) VALUES (?, ?)", (order_id, item_id))

conn.commit()
conn.close()
print("Database initialized successfully!")


# This script initializes the SQLite database with the schema and data from example_orders.json.
# It creates the necessary tables and populates them with the provided order data.
# The script handles the creation of customers, items, orders, and order_items tables,
# ensuring that all foreign key relationships are maintained.
# It also ensures that duplicate customers and items are not inserted into the database.
# The database is stored in a file named db.sqlite.
# The script uses the sqlite3 library to interact with the SQLite database.
# The JSON file example_orders.json should be in the same directory as this script.
# The script uses the INSERT OR IGNORE statement to avoid duplicate entries for customers and items.

