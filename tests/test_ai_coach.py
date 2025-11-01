"""
Unit tests for the AICoach class
"""

import unittest
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stardom_flow import AICoach


class TestAICoach(unittest.TestCase):
    """Test cases for the AICoach class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.coach = AICoach()
    
    def test_initialization(self):
        """Test AICoach initialization."""
        self.assertIsInstance(self.coach, AICoach)
        self.assertEqual(self.coach.user_data, {})
        self.assertEqual(self.coach.daily_schedule, {})
        self.assertIn('wake_time', self.coach.preferences)
        self.assertEqual(self.coach.preferences['wake_time'], '07:00')
    
    def test_learn_user_habits(self):
        """Test learning user habits."""
        test_data = {
            "name": "John Doe",
            "occupation": "Developer",
            "goals": ["productivity", "health"]
        }
        self.coach.learn_user_habits(test_data)
        self.assertEqual(self.coach.user_data['name'], 'John Doe')
        self.assertEqual(self.coach.user_data['occupation'], 'Developer')
    
    def test_learn_user_habits_with_preferences(self):
        """Test learning habits with preferences."""
        test_data = {
            "name": "Jane Doe",
            "preferences": {
                "wake_time": "06:00",
                "sleep_time": "23:00"
            }
        }
        self.coach.learn_user_habits(test_data)
        self.assertEqual(self.coach.preferences['wake_time'], '06:00')
        self.assertEqual(self.coach.preferences['sleep_time'], '23:00')
    
    def test_generate_daily_schedule(self):
        """Test daily schedule generation."""
        schedule = self.coach.generate_daily_schedule()
        
        # Check that schedule has expected periods
        self.assertIn('morning', schedule)
        self.assertIn('afternoon', schedule)
        self.assertIn('evening', schedule)
        
        # Check that each period has tasks
        self.assertGreater(len(schedule['morning']), 0)
        self.assertGreater(len(schedule['afternoon']), 0)
        self.assertGreater(len(schedule['evening']), 0)
        
        # Check task structure
        first_task = schedule['morning'][0]
        self.assertIn('time', first_task)
        self.assertIn('task', first_task)
    
    def test_set_reminders(self):
        """Test setting reminders."""
        reminders = self.coach.set_reminders()
        
        # Check that reminders were created
        self.assertIsInstance(reminders, list)
        self.assertGreater(len(reminders), 0)
        
        # Check reminder format
        self.assertIn('-', reminders[0])
    
    def test_adjust_schedule_skip_task(self):
        """Test skipping a task in the schedule."""
        # First generate a schedule
        self.coach.generate_daily_schedule()
        
        # Get initial morning task count
        initial_morning_count = len(self.coach.daily_schedule['morning'])
        
        # Skip a task
        feedback = {"skip_tasks": ["Workout"]}
        self.coach.adjust_schedule(feedback)
        
        # Check that a task was removed
        final_morning_count = len(self.coach.daily_schedule['morning'])
        self.assertLess(final_morning_count, initial_morning_count)
    
    def test_adjust_schedule_add_task(self):
        """Test adding a task to the schedule."""
        # First generate a schedule
        self.coach.generate_daily_schedule()
        
        # Get initial afternoon task count
        initial_afternoon_count = len(self.coach.daily_schedule['afternoon'])
        
        # Add a task
        feedback = {
            "add_tasks": [{
                "period": "afternoon",
                "time": "16:00",
                "task": "Team meeting"
            }]
        }
        self.coach.adjust_schedule(feedback)
        
        # Check that a task was added
        final_afternoon_count = len(self.coach.daily_schedule['afternoon'])
        self.assertEqual(final_afternoon_count, initial_afternoon_count + 1)
    
    def test_adjust_schedule_reschedule_task(self):
        """Test rescheduling a task."""
        # First generate a schedule
        self.coach.generate_daily_schedule()
        
        # Reschedule a task
        feedback = {
            "reschedule": [{
                "task_name": "Lunch",
                "new_time": "13:30"
            }]
        }
        self.coach.adjust_schedule(feedback)
        
        # Check that the task was rescheduled
        lunch_task = None
        for task in self.coach.daily_schedule['afternoon']:
            if 'Lunch' in task['task']:
                lunch_task = task
                break
        
        self.assertIsNotNone(lunch_task)
        self.assertEqual(lunch_task['time'], '13:30')
    
    def test_get_schedule_summary(self):
        """Test getting schedule summary."""
        summary = self.coach.get_schedule_summary()
        
        # Check that summary is a string
        self.assertIsInstance(summary, str)
        
        # Check that summary contains expected sections
        self.assertIn('MORNING', summary)
        self.assertIn('AFTERNOON', summary)
        self.assertIn('EVENING', summary)
    
    def test_add_minutes(self):
        """Test the _add_minutes helper method."""
        result = self.coach._add_minutes("10:00", 30)
        self.assertEqual(result, "10:30")
        
        result = self.coach._add_minutes("23:30", 45)
        self.assertEqual(result, "00:15")
    
    def test_remove_task(self):
        """Test the _remove_task helper method."""
        self.coach.generate_daily_schedule()
        initial_count = len(self.coach.daily_schedule['morning'])
        
        self.coach._remove_task("Workout")
        
        final_count = len(self.coach.daily_schedule['morning'])
        self.assertLess(final_count, initial_count)


if __name__ == '__main__':
    unittest.main()
