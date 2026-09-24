import time
import threading
import multiprocessing
import asyncio


# I/O-bound task (Simulates network request or file read)
def io_task():
    time.sleep(1)

# Async I/O-bound task
async def async_io_task():
    await asyncio.sleep(1)

# CPU-bound task 
def cpu_task():
    return sum(i * i for i in range(10**7))

# --- Implementations ---

# 1. Threading Implementation 
def run_threading():
    start_time = time.time()
    threads = [threading.Thread(target=io_task) for _ in range(5)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print(f"Threading (I/O-bound) Execution Time: {time.time() - start_time:.4f} seconds")

# 2. Multiprocessing Implementation 
def run_multiprocessing():
    start_time = time.time()
    processes = [multiprocessing.Process(target=cpu_task) for _ in range(5)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
        
    print(f"Multiprocessing (CPU-bound) Execution Time: {time.time() - start_time:.4f} seconds")

# 3. AsyncIO Implementation 
async def run_asyncio():
    start_time = time.time()
    tasks = [async_io_task() for _ in range(5)]
    await asyncio.gather(*tasks)
    
    print(f"AsyncIO (I/O-bound) Execution Time: {time.time() - start_time:.4f} seconds")

# --- CPU-bound Baseline (Sequential) for Comparison ---
def run_sequential_cpu():
    start_time = time.time()
    for _ in range(5):
        cpu_task()
    print(f"Sequential (CPU-bound) Execution Time: {time.time() - start_time:.4f} seconds")

if __name__ == "__main__":
    print("Running Concurrency Tests...\n")
    
    run_threading()
    asyncio.run(run_asyncio())
    
    print("\n--- CPU-Bound Comparison ---")
    run_sequential_cpu()
    run_multiprocessing()
