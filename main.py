
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Customer(BaseModel):
    name: str
    phone: str

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    customer_id: int
    timestamp: int
    notes: str = ""

def get_db_connection():
    conn = sqlite3.connect('db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

# Customers endpoints
@app.post("/customers")
def create_customer(customer: Customer):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (customer.name, customer.phone))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Phone number already exists.")
    return {"message": "Customer created successfully."}

@app.get("/customers/{id}")
def read_customer(id: int):
    conn = get_db_connection()
    customer = conn.execute("SELECT * FROM customers WHERE id = ?", (id,)).fetchone()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found.")
    return dict(customer)

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customer):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE customers SET name = ?, phone = ? WHERE id = ?", (customer.name, customer.phone, id))
    conn.commit()
    return {"message": "Customer updated successfully."}

@app.delete("/customers/{id}")
def delete_customer(id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE id = ?", (id,))
    conn.commit()
    return {"message": "Customer deleted successfully."}

# Items endpoints
@app.post("/items")
def create_item(item: Item):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Item name already exists.")
    return {"message": "Item created successfully."}

@app.get("/items/{id}")
def read_item(id: int):
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    return dict(item)

@app.put("/items/{id}")
def update_item(id: int, item: Item):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE items SET name = ?, price = ? WHERE id = ?", (item.name, item.price, id))
    conn.commit()
    return {"message": "Item updated successfully."}

@app.delete("/items/{id}")
def delete_item(id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    return {"message": "Item deleted successfully."}

# Orders endpoints
@app.post("/orders")
def create_order(order: Order):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (customer_id, timestamp, notes) VALUES (?, ?, ?)", 
                (order.customer_id, order.timestamp, order.notes))
    conn.commit()
    return {"message": "Order created successfully."}

@app.get("/orders/{id}")
def read_order(id: int):
    conn = get_db_connection()
    order = conn.execute("SELECT * FROM orders WHERE id = ?", (id,)).fetchone()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")
    return dict(order)

@app.put("/orders/{id}")
def update_order(id: int, order: Order):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE orders SET customer_id = ?, timestamp = ?, notes = ? WHERE id = ?", 
                (order.customer_id, order.timestamp, order.notes, id))
    conn.commit()
    return {"message": "Order updated successfully."}

@app.delete("/orders/{id}")
def delete_order(id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM orders WHERE id = ?", (id,))
    conn.commit()
    return {"message": "Order deleted successfully."}
