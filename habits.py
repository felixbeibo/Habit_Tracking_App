from datetime import date, timedelta

class Habit:
    """
    Represents a habit that a user wants to track.

    Attributes:
        name (str): The name of the habit.
        frequency (int): How often (in days) the habit should be completed.
        completions (list of date): A list of dates when the habit was completed.
    """

    def __init__(self, name: str, frequency: int):
        self.name = name
        self.frequency = frequency  # in days
        self.completions = []

    def mark_completed(self):
        """Marks the habit as completed for today if not already marked."""
        today = date.today()
        if today not in self.completions:
            self.completions.append(today)

    def get_streak(self, tolerance_days=0):
        """
        Calculates the current streak of consecutive completions
        based on the frequency in days and optional tolerance.

        Args:
            tolerance_days (int): Days of leeway allowed after the expected interval.

        Returns:
            int: The current streak count.
        """
        if not self.completions:
            return 0

        sorted_dates = sorted(self.completions, reverse=True)
        streak = 1
        current = sorted_dates[0]

        for d in sorted_dates[1:]:
            delta = (current - d).days
            if self.frequency <= delta <= self.frequency + tolerance_days:
                streak += 1
                current = d
            else:
                break
        return streak

    def to_dict(self):
        """Converts the Habit instance to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'frequency': self.frequency,
            'completions': [d.isoformat() for d in self.completions]
        }

    @staticmethod
    def from_dict(data):
        """Creates a Habit instance from a dictionary."""
        habit = Habit(data['name'], data['frequency'])
        habit.completions = [date.fromisoformat(d) for d in data['completions']]
        return habit
