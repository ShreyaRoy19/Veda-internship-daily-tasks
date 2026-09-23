# Concurrent URL Checker

## Description
A Python utility that checks the availability and response time of multiple URLs concurrently. This project demonstrates practical concurrency and network programming using Python's `ThreadPoolExecutor` to handle I/O-bound tasks efficiently.

## Features
* **Concurrent Execution:** Processes multiple URL requests simultaneously without creating an excessive number of threads.
* **Status-Code Report:** Retrieves and displays the HTTP status code for each successful request.
* **Response-Time Report:** Calculates and displays the time taken for each request.
* **Failure Handling:** Gracefully handles invalid URLs, network errors, and server timeouts.
* **Configurable Timeouts:** Uses request timeouts to prevent hanging on unresponsive servers.

## Prerequisites
* Python 3.x
* `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
