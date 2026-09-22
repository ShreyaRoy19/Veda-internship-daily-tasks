import time

def generate_report(report_id: int):
    """Simulates a heavy report generation process."""
    print(f"Starting report generation for ID: {report_id}...")
    time.sleep(5)  # Simulate blocking work
    print(f"Report {report_id} generated successfully!")
    return f"Report {report_id} completed."

def send_email(email: str, message: str):
    """Simulates sending an email."""
    print(f"Sending email to {email}...")
    time.sleep(3)
    print(f"Email sent successfully to {email}!")
    return f"Email to {email} sent."
