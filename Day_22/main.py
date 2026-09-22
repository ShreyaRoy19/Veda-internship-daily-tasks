from fastapi import FastAPI, HTTPException
import redis
from rq import Queue
from rq.job import Job
from tasks import generate_report, send_email

app = FastAPI(title="Background Job Processor")

# Connect to Redis and set up the queue
redis_conn = redis.Redis(host='localhost', port=6379, db=0)
task_queue = Queue('default', connection=redis_conn)

@app.post("/submit-report/")
def submit_report(report_id: int):
    """Endpoint to submit a background report generation job."""
    job = task_queue.enqueue(generate_report, report_id)
    return {
        "message": "Report generation job submitted successfully!",
        "job_id": job.get_id(),
        "status": job.get_status()
    }

@app.post("/send-email/")
def submit_email(email: str, message: str):
    """Endpoint to submit an email sending job."""
    job = task_queue.enqueue(send_email, email, message)
    return {
        "message": "Email job submitted successfully!",
        "job_id": job.get_id(),
        "status": job.get_status()
    }

@app.get("/job-status/{job_id}")
def get_job_status(job_id: str):
    """Endpoint to track job status and execution logs/results."""
    try:
        job = Job.fetch(job_id, connection=redis_conn)
    except Exception:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "job_id": job.get_id(),
        "status": job.get_status(),  # queued, started, finished, failed
        "result": job.result,        # Return value if finished
        "error": str(job.exc_info) if job.is_failed else None
    }
