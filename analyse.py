def get_all_streaks(habits, tolerance_days=0):
    """Returns a dictionary mapping each habit's name to its current streak."""
    return {habit.name: habit.get_streak(tolerance_days=tolerance_days) for habit in habits}

def get_highest_streak(habits, tolerance_days=0):
    """Returns the habit with the highest current streak."""
    if not habits:
        return None
    return max(habits, key=lambda h: h.get_streak(tolerance_days=tolerance_days))

def filter_by_frequency(habits, frequency):
    """Filters and returns habits that match the given frequency in days."""
    return [habit for habit in habits if habit.frequency == frequency]
