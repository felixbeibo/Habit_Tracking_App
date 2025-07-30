# Habit Tracking App

This is a terminal-based habit tracking application written in Python. It helps users define and track recurring habits over time, calculate streaks, and export data to JSON. The application uses a simple command-line interface powered by `questionary`.

## Features

- Create, manage, and delete habits  
- Flexible habit frequency (e.g., every 1, 3, 7 days)  
- Streak tracking with configurable tolerance window (± days)  
- Load predefined habit templates  
- Export habits to JSON  
- Fully testable code with `pytest`  
- Modular design separating logic (OOP) and analysis (FP)

## Project Structure

habit_tracker/  
├── main.py            # Main CLI application  
├── habits.py          # Habit class and logic  
├── analyse.py         # Analytics functions (e.g. streak calculation)  
├── db.py              # JSON storage for habits  
├── templates.py       # Predefined habit templates  
├── test_project.py    # Unit tests for habit logic  
├── requirements.txt   # Required dependencies  
├── readme.md          # Project documentation  

## Installation & Setup

To run the project locally:

1. Clone the repository  
`git clone https://github.com/YOUR_USERNAME/habit-tracker-cli.git`  
`cd habit-tracker-cli`  

2. Set up a virtual environment (recommended)  
`python -m venv venv`  
`source venv/bin/activate` (Windows: `venv\Scripts\activate`)  

3. Install dependencies  
`pip install -r requirements.txt`  

4. Start the application  
`python main.py`  

## How to Use

Once started, you will see a menu-based CLI interface. Use the arrow keys to choose between options:

- Create a new habit by providing a name and frequency (in days)  
- Mark existing habits as completed  
- View all streaks or the highest current streak  
- Load predefined template habits  
- Export all data to JSON  
- Adjust the tolerance for streaks (± days)  

Habits are stored in a local `habits.json` file.

## Running Tests

All core logic has been covered with unit tests using `pytest`. To run the tests:  
`pytest test_project.py`  

Expected output:  
`5 passed in 0.01s`  

The application has been successfully tested using pytest. All unit tests passed.

## Reflection & Documentation

This project was implemented during a course on Object-Oriented and Functional Programming with Python.  
You can find the full technical reflection and explanation of implementation in the [Reflection Paper](INSERT_LINK_HERE).

## GitHub Repository

View the full source code and history on GitHub:  
**[https://github.com/YOUR_USERNAME/habit-tracker-cli](https://github.com/YOUR_USERNAME/habit-tracker-cli)**

## License

This project is open-source and uses the MIT License.

## Python Version

Tested with: Python 3.12+
