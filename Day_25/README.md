# Build a Retry and Timeout System for API Calls

A resilient network programming module featuring a reusable API client with configurable request timeouts, retries, exponential backoff, and clear failure handling.

---

## 📌 Deliverables Covered

- [x] **Reusable API client** (`ResilientApiClient` class)
- [x] **Timeout configuration** (configurable connection and read timeouts)
- [x] **Retry logic** (maximum retry count and selective HTTP error filtering)
- [x] **Backoff implementation** (exponential backoff with randomized jitter)
- [x] **Logging** (clear standard logging across attempts, retries, and errors)

---

## 🛠️ Requirements & Installation

- Python 3.8+
- `requests` library

```bash
pip install requests
