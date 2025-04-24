
#  Testing Guide for Dosa Restaurant REST API

This guide provides example `curl` commands to test the CRUD operations for Customers, Items, and Orders.

---

##  Running  API
1. Activate  virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

2. Start  FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

---

##  Customers API

###  Add Customer (POST)
```bash
curl -X POST "http://127.0.0.1:8000/customers" -H "Content-Type: application/json" -d "{"name": "Ravi", "phone": "9998887777"}"
```

###  Get Customer by ID (GET)
```bash
curl "http://127.0.0.1:8000/customers/1"
```

###  Update Customer by ID (PUT)
```bash
curl -X PUT "http://127.0.0.1:8000/customers/1" -H "Content-Type: application/json" -d "{"name": "Ravi Kumar", "phone": "9998887777"}"
```

###  Delete Customer by ID (DELETE)
```bash
curl -X DELETE "http://127.0.0.1:8000/customers/1"
```

---

##  Items API

###  Add Item (POST)
```bash
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d "{"name": "Masala Dosa", "price": 7.99}"
```

###  Get Item by ID (GET)
```bash
curl "http://127.0.0.1:8000/items/1"
```

###  Update Item by ID (PUT)
```bash
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d "{"name": "Onion Masala Dosa", "price": 8.99}"
```

###  Delete Item by ID (DELETE)
```bash
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

---

##  Orders API

###  Add Order (POST)
```bash
curl -X POST "http://127.0.0.1:8000/orders" -H "Content-Type: application/json" -d "{"customer_id": 1, "timestamp": 1713986200, "notes": "Extra chutney please!"}"
```

###  Get Order by ID (GET)
```bash
curl "http://127.0.0.1:8000/orders/1"
```

###  Update Order by ID (PUT)
```bash
curl -X PUT "http://127.0.0.1:8000/orders/1" -H "Content-Type: application/json" -d "{"customer_id": 1, "timestamp": 1713986201, "notes": "No onions"}"
```

###  Delete Order by ID (DELETE)
```bash
curl -X DELETE "http://127.0.0.1:8000/orders/1"
```

---

Reminder: The IDs (1 in the examples) are just sample values. Please check your database for the correct IDs when testing.
