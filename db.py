import json
import os
from habits import Habit

DATA_FILE = 'habits.json'

def save_habits(habits):
    """Saves a list of Habit instances to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump([habit.to_dict() for habit in habits], f, indent=4)

def load_habits():
    """Loads Habit instances from the JSON file if it exists, otherwise returns an empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return [Habit.from_dict(h) for h in data]
