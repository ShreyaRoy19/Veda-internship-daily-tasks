# FastAPI Rate-Limiter API

A lightweight, high-performance API rate limiter built with **Python**, **FastAPI**, and an in-memory sliding window algorithm. This application restricts excessive requests from individual client IPs to protect backend resources from abuse[cite: 1].

---

## Features

* **IP-Based Tracking:** Tracks and limits incoming requests based on the client's IP address[cite: 1].
* **Sliding Window Algorithm:** Dynamically cleans up expired request timestamps to allow normal traffic flow after the window resets[cite: 1].
* **HTTP 429 Handling:** Automatically responds with a standard `429 Too Many Requests` status code and error message when a client crosses the threshold[cite: 1].

---

## Tech Stack

* **Python 3.x**
* **FastAPI**
* **Uvicorn** (ASGI server)

---

## Project Structure

```text
task_manager_api/
│
├── main.py        # Main FastAPI application & rate-limiting middleware
└── README.md      # Project documentation
