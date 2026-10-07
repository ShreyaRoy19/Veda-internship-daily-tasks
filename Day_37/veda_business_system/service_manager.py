import json
import os

DATA_FILE = os.path.join("data", "services.json")

class ServiceManager:
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

    def add_service(self, service_id, name, category, price, status="Active"):
        services = self._load_data()
        if any(s["id"] == service_id for s in services):
            raise ValueError(f"Service with ID '{service_id}' already exists.")
        
        service = {
            "id": service_id,
            "name": name,
            "category": category,
            "price": float(price),
            "status": status
        }
        services.append(service)
        self._save_data(services)
        return service

    def list_services(self):
        return self._load_data()

    def filter_services(self, category=None, status=None):
        services = self._load_data()
        results = services
        if category:
            results = [s for s in results if s["category"].lower() == category.lower()]
        if status:
            results = [s for s in results if s["status"].lower() == status.lower()]
        return results
