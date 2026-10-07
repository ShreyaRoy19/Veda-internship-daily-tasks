import json
import os
from datetime import datetime

DATA_FILE = os.path.join("data", "inquiries.json")

class InquiryManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(DATA_FILE):
            self._save_data([])

    def _load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self, data):
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def log_inquiry(self, inquiry_id, client_name, email, service_or_prog, details):
        inquiries = self._load_data()
        if any(i["id"] == inquiry_id for i in inquiries):
            raise ValueError(f"Inquiry ID '{inquiry_id}' already exists.")

        inquiry = {
            "id": inquiry_id,
            "client_name": client_name,
            "email": email,
            "target": service_or_prog,
            "details": details,
            "status": "Pending",  # 'Pending', 'In Progress', 'Resolved'
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        inquiries.append(inquiry)
        self._save_data(inquiries)
        return inquiry

    def update_status(self, inquiry_id, new_status):
        inquiries = self._load_data()
        for item in inquiries:
            if item["id"] == inquiry_id:
                item["status"] = new_status
                self._save_data(inquiries)
                return True
        raise KeyError(f"Inquiry ID '{inquiry_id}' not found.")

    def list_inquiries(self):
        return self._load_data()

    def filter_by_status(self, status):
        inquiries = self._load_data()
        return [i for i in inquiries if i["status"].lower() == status.lower()]
