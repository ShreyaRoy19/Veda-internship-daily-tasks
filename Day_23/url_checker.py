import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_url(url, timeout=5):
    """
    Checks the availability and response time of a single URL.
    Includes failure handling and request timeouts.
    """
    start_time = time.time()
    try:
        # Set request timeouts to prevent hanging on slow servers
        response = requests.get(url, timeout=timeout)
        response_time = time.time() - start_time
        return {
            'url': url,
            'status_code': response.status_code,
            'response_time': response_time,
            'error': None
        }
    except requests.exceptions.RequestException as e:
        # Failure handling for network issues, invalid URLs, or timeouts
        response_time = time.time() - start_time
        return {
            'url': url,
            'status_code': None,
            'response_time': response_time,
            'error': str(e)
        }

def run_concurrent_checker(urls, max_threads=5):
    """
    Executes the URL checks concurrently. 
    Controls the number of threads to avoid excessive creation.
    """
    results = []
    
    # Using ThreadPoolExecutor for I/O-bound concurrent tasks
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Submit tasks to the executor
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        
        # Collect results as they complete
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                results.append(future.result())
            except Exception as exc:
                results.append({'url': url, 'status_code': None, 'response_time': None, 'error': str(exc)})
                
    return results

if __name__ == "__main__":
    
    urls_to_test = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.google.com",
        "https://this-is-an-invalid-domain-name-test.com", 
        "http://httpbin.org/delay/10" 
    ]
    
    print("Starting Concurrent URL Checks...")
    
   
    report = run_concurrent_checker(urls_to_test, max_threads=5)
    
    print("\n--- URL Checker Report ---")
    for data in report:
        if data['error']:
            print(f"[FAILED] {data['url']} | Error: {data['error']} | Time: {data['response_time']:.2f}s")
        else:
            print(f"[SUCCESS] {data['url']} | Status: {data['status_code']} | Time: {data['response_time']:.2f}s")
