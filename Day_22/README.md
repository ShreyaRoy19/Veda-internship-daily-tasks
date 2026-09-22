# Background Job Processor

A Python application built with **FastAPI** and **RQ (Redis Queue)** that offloads time-consuming tasks (such as report generation and email processing) into asynchronous background jobs to keep API responses fast and non-blocking[cite: 1].

---

## 🚀 Features

* **Asynchronous Processing**: Move heavy workloads away from the main API request thread[cite: 1].
* **Task Submission Endpoints**: Easily trigger background tasks like report generation and email sending via REST endpoints.
* **Job Status Tracking**: Check the real-time status (`queued`, `started`, `finished`, or `failed`) of any job using its unique `job_id`.
* **Error Handling & Logs**: View execution logs and exception traces if a background task fails.

---

## 🛠️ Tech Stack

* **Python**[cite: 1]
* **FastAPI** (Web framework)[cite: 1]
* **Redis** (In-memory data store / message broker)
* **RQ (Redis Queue)** (Library for queueing jobs and processing them with workers)[cite: 1]
* **Uvicorn** (ASGI server)

---

## 📁 Project Structure

```text
background_job_project/
│
├── worker.py          # RQ worker that listens to the queue and executes jobs
├── tasks.py           # Background task definitions (reports, emails, etc.)
├── main.py            # FastAPI app containing submission & tracking endpoints
└── README.md          # Project documentation
