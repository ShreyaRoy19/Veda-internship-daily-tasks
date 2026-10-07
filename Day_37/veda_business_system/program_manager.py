import json
import os

DATA_FILE = os.path.join("data", "programs.json")

class ProgramManager:
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

    def add_program(self, program_id, title, program_type, duration_weeks, seats):
        programs = self._load_data()
        if any(p["id"] == program_id for p in programs):
            raise ValueError(f"Program with ID '{program_id}' already exists.")

        program = {
            "id": program_id,
            "title": title,
            "type": program_type,  # e.g., 'Internship', 'Training'
            "duration_weeks": int(duration_weeks),
            "available_seats": int(seats)
        }
        programs.append(program)
        self._save_data(programs)
        return program

    def list_programs(self):
        return self._load_data()

    def filter_programs(self, program_type=None):
        programs = self._load_data()
        if program_type:
            return [p for p in programs if p["type"].lower() == program_type.lower()]
        return programs
