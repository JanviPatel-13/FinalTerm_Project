
# Dosa Restaurant REST API

This project is a REST API backend for a dosa restaurant built using FastAPI and SQLite. 
It supports CRUD operations for customers, items, and orders.

## How to run

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Initialize the database:
   ```bash
   python init_db.py
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Test your endpoints using curl or any REST client like Postman.

## Endpoints
- POST /customers
- GET /customers/{id}
- PUT /customers/{id}
- DELETE /customers/{id}
- POST /items
- GET /items/{id}
- PUT /items/{id}
- DELETE /items/{id}
- POST /orders
- GET /orders/{id}
- PUT /orders/{id}
- DELETE /orders/{id}
