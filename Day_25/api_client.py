import logging
import random
import time
from typing import Any, Dict, Optional, Set
import requests
from requests.exceptions import ConnectionError, RequestException, Timeout

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("ResilientApiClient")


class ApiClientError(Exception):
    """Base exception for client errors."""


class MaxRetriesExceededError(ApiClientError):
    """Raised when maximum retry attempts are exhausted."""


class ResilientApiClient:
    """A resilient HTTP client with timeouts, retries, and exponential backoff."""

    # Retrying transient server errors and rate limits; do NOT retry 4xx client errors (e.g., 400, 401, 403, 404)
    RETRYABLE_STATUS_CODES: Set[int] = {429, 500, 502, 503, 504}

    def __init__(
        self,
        base_url: str = "",
        timeout: float = 5.0,
        max_retries: int = 3,
        backoff_factor: float = 1.0,
        max_backoff: float = 30.0,
    ):
        """
        :param base_url: Common prefix for request URLs.
        :param timeout: Network timeout in seconds for connect & read.
        :param max_retries: Maximum number of retry attempts after the first failure.
        :param backoff_factor: Multiplier for exponential backoff calculation.
        :param max_backoff: Maximum delay cap in seconds.
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.max_backoff = max_backoff
        self.session = requests.Session()

    def _calculate_backoff(self, attempt: int) -> float:
        """
        Calculates exponential backoff with full jitter to avoid the thundering herd problem:
        delay = min(max_backoff, backoff_factor * 2 ** attempt) + random jitter
        """
        delay = min(self.max_backoff, self.backoff_factor * (2**attempt))
        jitter = random.uniform(0, 0.5 * delay)
        return delay + jitter

    def request(
        self,
        method: str,
        endpoint: str,
        timeout: Optional[float] = None,
        **kwargs: Any,
    ) -> requests.Response:
        """
        Executes an HTTP request with retry and backoff logic.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}" if self.base_url else endpoint
        req_timeout = timeout if timeout is not None else self.timeout
        total_attempts = self.max_retries + 1

        for attempt in range(total_attempts):
            try:
                logger.info(
                    "Sending %s request to %s (Attempt %d/%d)",
                    method.upper(),
                    url,
                    attempt + 1,
                    total_attempts,
                )

                response = self.session.request(
                    method=method.upper(),
                    url=url,
                    timeout=req_timeout,
                    **kwargs,
                )

                # Check if the HTTP status warrants a retry (e.g., 5xx or 429)
                if response.status_code in self.RETRYABLE_STATUS_CODES:
                    logger.warning(
                        "Received retryable status %d from %s",
                        response.status_code,
                        url,
                    )
                    if attempt < self.max_retries:
                        sleep_time = self._calculate_backoff(attempt)
                        logger.info("Backing off for %.2f seconds...", sleep_time)
                        time.sleep(sleep_time)
                        continue
                    else:
                        response.raise_for_status()

                # Raise an error for non-retryable 4xx errors immediately without retrying
                response.raise_for_status()
                return response

            except (Timeout, ConnectionError) as exc:
                logger.warning(
                    "Network error on attempt %d: %s", attempt + 1, str(exc)
                )
                if attempt < self.max_retries:
                    sleep_time = self._calculate_backoff(attempt)
                    logger.info("Backing off for %.2f seconds...", sleep_time)
                    time.sleep(sleep_time)
                else:
                    logger.error("Max retries reached. Operation failed.")
                    raise MaxRetriesExceededError(
                        f"Request to {url} failed after {total_attempts} attempts: {exc}"
                    ) from exc

            except requests.HTTPError as exc:
                # Non-retryable HTTP error (e.g. 400 Bad Request, 404 Not Found)
                logger.error("Non-retryable HTTP error encountered: %s", str(exc))
                raise

            except RequestException as exc:
                logger.error("Unrecoverable request error: %s", str(exc))
                raise ApiClientError(f"Request failed: {exc}") from exc

        raise MaxRetriesExceededError(
            f"Request failed after {total_attempts} attempts."
        )

    # Convenience shortcuts
    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.request("DELETE", endpoint, **kwargs)

    def close(self):
        """Clean up the underlying connection pool."""
        self.session.close()


# Example Usage & Testing
if __name__ == "__main__":
    client = ResilientApiClient(
        base_url="https://httpbin.org",
        timeout=3.0,
        max_retries=2,
        backoff_factor=1.0,
    )

    # 1. Successful request
    try:
        print("\n--- Test 1: Successful Request ---")
        res = client.get("/status/200")
        print(f"Status: {res.status_code}")
    except Exception as e:
        print(f"Error: {e}")

    # 2. Transient error that triggers retries (Status 503)
    try:
        print("\n--- Test 2: Retryable Status 503 ---")
        client.get("/status/503")
    except Exception as e:
        print(f"Caught expected failure: {type(e).__name__}")

    # 3. Non-retryable error (Status 404 should fail immediately)
    try:
        print("\n--- Test 3: Non-retryable Status 404 ---")
        client.get("/status/404")
    except Exception as e:
        print(f"Caught expected failure: {type(e).__name__}")

    client.close()
