from fastapi import FastAPI, Request
import logging
import time

# Initialize the FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Middleware to log requests
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Simple GET route
@app.get("/hello")
async def read_hello():
    return {"message": "Hello, FastAPI with Middleware!"}

# Another example route
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "message": "Item fetched successfully"}
