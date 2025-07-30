import questionary
from db import load_habits, save_habits
from habits import Habit
from analyse import get_all_streaks, get_highest_streak, filter_by_frequency

# Welcome message
print("\n👋 Welcome to the Habit Tracker CLI!\n")

# Load existing habits and initialize tolerance setting
habits = load_habits()
TOLERANCE_DAYS = 1

# Start the main menu loop
while True:
    choice = questionary.select(
        "What would you like to do?",
        choices=[
            "Create new habit",
            "Mark habit as complete",
            "Show all streaks",
            "Show highest streak",
            "Set streak tolerance (± days)",
            "Export habits",
            "Exit"
        ]).ask()

    # Create a new habit
    if choice == "Create new habit":
        name = questionary.text("Enter habit name:").ask()
        frequency_input = questionary.text("How often should this habit be done? (Enter number of days):").ask()
        try:
            frequency = int(frequency_input)
            habits.append(Habit(name, frequency))
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Mark a habit as completed today
    elif choice == "Mark habit as complete":
        if not habits:
            print("No habits found. Please create one first.")
            continue
        habit_name = questionary.select("Which habit?", choices=[h.name for h in habits]).ask()
        for h in habits:
            if h.name == habit_name:
                h.mark_completed()
                print(f"Marked '{h.name}' as complete.")
                break

    # Display streaks for all habits
    elif choice == "Show all streaks":
        for name, streak in get_all_streaks(habits, tolerance_days=TOLERANCE_DAYS).items():
            print(f"{name}: {streak} streak(s) (±{TOLERANCE_DAYS} day tolerance)")

    # Display the highest streak
    elif choice == "Show highest streak":
        top = get_highest_streak(habits, tolerance_days=TOLERANCE_DAYS)
        if top:
            print(f"🏆 Highest streak: {top.name} ({top.get_streak(tolerance_days=TOLERANCE_DAYS)} streaks, every {top.frequency} days)")

    # Set user-configurable tolerance value
    elif choice == "Set streak tolerance (± days)":
        tolerance_input = questionary.text("Enter tolerance in days (e.g., 0 for strict, 1 for slight delay):").ask()
        try:
            TOLERANCE_DAYS = int(tolerance_input)
            print(f"✅ Tolerance set to ±{TOLERANCE_DAYS} day(s).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Export all current habits to JSON file
    elif choice == "Export habits":
        save_habits(habits)
        print("✅ Habits exported to JSON.")

    # Exit the program and save current habits
    elif choice == "Exit":
        save_habits(habits)
        print("👋 Goodbye!")
        break
