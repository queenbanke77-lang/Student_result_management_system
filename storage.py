import json
import os
from student import Student

DATA_FILE = "data/students.json"

def save_data(students_dict):
    """Save students dictionary to JSON file."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        data_to_save = {sid: s.to_dict() for sid, s in students_dict.items()}
        with open(DATA_FILE, 'w') as file:
            json.dump(data_to_save, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data():
    """Load students dictionary from JSON file. Handle missing file gracefully."""
    students_dict = {}
    if not os.path.exists(DATA_FILE):
        return students_dict
    
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            for sid, s_dict in data.items():
                students_dict[sid] = Student.from_dict(s_dict)
    except json.JSONDecodeError:
        print("Error: Data file is corrupted or empty. Starting with an empty record.")
    except Exception as e:
        print(f"An unexpected error occurred while loading data: {e}")
    
    return students_dict