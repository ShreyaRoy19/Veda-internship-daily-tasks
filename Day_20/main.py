from fastapi import FastAPI, Request, HTTPException, status
import time
from collections import defaultdict

app = FastAPI(title="Rate-Limited API")

request_records = defaultdict(list)
WINDOW_SIZE_SECONDS = 60
MAX_REQUESTS = 5

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    current_time = time.time()

    timestamps = request_records[client_ip]
    while timestamps and timestamps[0] < current_time - WINDOW_SIZE_SECONDS:
        timestamps.pop(0)

    if len(timestamps) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Too many requests, please try again later."
        )

    timestamps.append(current_time)
    response = await call_next(request)
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome! You are accessing a rate-limited endpoint."}
