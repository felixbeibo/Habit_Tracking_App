import unittest
from habits import Habit
from datetime import date, timedelta

class TestHabit(unittest.TestCase):
    """Unit tests for the Habit class methods."""

    def setUp(self):
        """Set up a test habit before each test."""
        self.habit = Habit("Test Habit", 1)

    def test_mark_completed(self):
        """Test if today's date is added when marked complete."""
        self.habit.mark_completed()
        self.assertIn(date.today(), self.habit.completions)

    def test_get_streak_single_day(self):
        """Test streak calculation for a single completion day."""
        self.habit.completions = [date.today()]
        self.assertEqual(self.habit.get_streak(), 1)

    def test_get_streak_consecutive_days(self):
        """Test streak for two consecutive completion days."""
        today = date.today()
        self.habit.completions = [today - timedelta(days=1), today]
        self.assertEqual(self.habit.get_streak(), 2)

    def test_get_streak_with_tolerance(self):
        """Test streak with a gap within tolerance limit."""
        today = date.today()
        self.habit.completions = [today - timedelta(days=2), today]
        self.assertEqual(self.habit.get_streak(tolerance_days=1), 2)

    def test_to_from_dict(self):
        """Test serialization and deserialization of habit data."""
        self.habit.mark_completed()
        data = self.habit.to_dict()
        new_habit = Habit.from_dict(data)
        self.assertEqual(new_habit.name, self.habit.name)
        self.assertEqual(new_habit.frequency, self.habit.frequency)
        self.assertEqual(new_habit.completions, self.habit.completions)

if __name__ == '__main__':
    unittest.main()
