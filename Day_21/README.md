# ⚡ FastAPI & Redis Caching Layer

> A high-performance demonstration of caching strategies, TTL configurations, and cache invalidation patterns using FastAPI and Redis.

---

## 🚀 Quick Copy-Paste Code

### `main.py`
```python
import time
import json
from fastapi import FastAPI, HTTPException
import redis

app = FastAPI(title="API Caching Layer with Redis")

# Initialize Redis connection
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

CACHE_EXPIRATION_SECONDS = 60  # Cache TTL configuration


def simulate_expensive_database_query(item_id: int):
    """Simulates a slow database call or heavy external request."""
    time.sleep(2)  # Simulating a 2-second delay
    database = {
        1: {"id": 1, "name": "Wireless Mouse", "price": 25.99, "stock": 120},
        2: {"id": 2, "name": "Mechanical Keyboard", "price": 79.99, "stock": 45},
        3: {"id": 3, "name": "HD Monitor", "price": 189.99, "stock": 15},
    }
    return database.get(item_id)


@app.get("/items/{item_id}")
def get_item(item_id: int):
    cache_key = f"item:{item_id}"
    
    # 1. Check the Cache Layer first (Cache Hit / Miss check)
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return {
            "source": "cache",
            "data": json.loads(cached_data)
        }
    
    # 2. If Cache Miss, fetch from the database
    item = simulate_expensive_database_query(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # 3. Store result back into Redis with a TTL expiration time
    redis_client.setex(cache_key, CACHE_EXPIRATION_SECONDS, json.dumps(item))
    
    return {
        "source": "database",
        "data": item
    }


@app.put("/items/{item_id}")
def update_item(item_id: int, price: float, stock: int):
    """
    Cache Invalidation Strategy:
    Invalidates/deletes the stale cache entry upon data updates.
    """
    cache_key = f"item:{item_id}"
    
    item = simulate_expensive_database_query(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item["price"] = price
    item["stock"] = stock
    
    # Invalidate cache so subsequent reads get fresh data
    redis_client.delete(cache_key)
    
    return {
        "message": "Item updated successfully and cache invalidated",
        "data": item
    }
