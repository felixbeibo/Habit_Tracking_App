from habits import Habit

def get_default_habits():
    """
    Returns a list of predefined Habit instances with frequency as days.
    
    These habits serve as initial templates for users who want to start quickly.
    """
    return [
        Habit("Drink Water", 1),             # daily
        Habit("Exercise", 2),               # every 2 days
        Habit("Meditate", 1),               # daily
        Habit("Read a Book", 3),            # every 3 days
        Habit("Go for a Walk", 1),          # daily
        Habit("Call Family", 7),            # weekly
        Habit("Clean Desk", 4),             # every 4 days
        Habit("Write Journal", 1),          # daily
        Habit("Learn Programming", 2),      # every 2 days
        Habit("Practice Music", 3)          # every 3 days
    ]
