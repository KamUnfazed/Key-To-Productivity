# AI Coach Framework for Stardom Flow
# This module contains the main structure and methods for the AI Coach.

from datetime import datetime, timedelta
from typing import Dict, List, Any


class AICoach:
    def __init__(self):
        self.user_data = {}
        self.daily_schedule = {}
        self.preferences = {
            "wake_time": "07:00",
            "sleep_time": "22:00",
            "work_hours": 8,
            "break_interval": 90  # minutes
        }
        self.reminders = []

    def learn_user_habits(self, data: Dict[str, Any]) -> None:
        """Process and integrate user data to learn habits."""
        self.user_data.update(data)
        
        # Update preferences if provided
        if "preferences" in data:
            self.preferences.update(data["preferences"])

    def generate_daily_schedule(self) -> Dict[str, List[Dict[str, str]]]:
        """Generate a structured daily schedule based on user data."""
        wake_time = self.preferences.get("wake_time", "07:00")
        sleep_time = self.preferences.get("sleep_time", "22:00")
        
        self.daily_schedule = {
            "morning": [
                {"time": wake_time, "task": "Wake up and morning routine"},
                {"time": self._add_minutes(wake_time, 30), "task": "Workout"},
                {"time": self._add_minutes(wake_time, 60), "task": "Breakfast"},
                {"time": self._add_minutes(wake_time, 90), "task": "Plan your day"}
            ],
            "afternoon": [
                {"time": "12:00", "task": "Lunch break"},
                {"time": "13:00", "task": "Focus work session"},
                {"time": "14:30", "task": "Short break"},
                {"time": "15:00", "task": "Continue focused work"}
            ],
            "evening": [
                {"time": "18:00", "task": "Dinner"},
                {"time": "19:00", "task": "Relaxation time"},
                {"time": "21:00", "task": "Daily reflection"},
                {"time": sleep_time, "task": "Prepare for sleep"}
            ]
        }
        return self.daily_schedule

    def set_reminders(self) -> List[str]:
        """Set reminders for tasks and activities."""
        self.reminders = []
        
        if not self.daily_schedule:
            self.generate_daily_schedule()
        
        for period, tasks in self.daily_schedule.items():
            for task in tasks:
                reminder = f"{task['time']} - {task['task']}"
                self.reminders.append(reminder)
        
        return self.reminders

    def adjust_schedule(self, feedback: Dict[str, Any]) -> None:
        """Dynamically adjust the schedule based on user feedback."""
        if "skip_tasks" in feedback:
            # Remove tasks from schedule
            for task_name in feedback["skip_tasks"]:
                self._remove_task(task_name)
        
        if "add_tasks" in feedback:
            # Add new tasks to schedule
            for task in feedback["add_tasks"]:
                self._add_task(task)
        
        if "reschedule" in feedback:
            # Modify task times
            for task_update in feedback["reschedule"]:
                self._reschedule_task(task_update)

    def _add_minutes(self, time_str: str, minutes: int) -> str:
        """Add minutes to a time string (HH:MM format)."""
        try:
            time_obj = datetime.strptime(time_str, "%H:%M")
            new_time = time_obj + timedelta(minutes=minutes)
            return new_time.strftime("%H:%M")
        except ValueError:
            # If invalid format, return original time
            return time_str

    def _remove_task(self, task_name: str) -> None:
        """Remove a task from the schedule."""
        for period in self.daily_schedule:
            self.daily_schedule[period] = [
                task for task in self.daily_schedule[period]
                if task_name.lower() not in task["task"].lower()
            ]

    def _add_task(self, task: Dict[str, str]) -> None:
        """Add a task to the schedule."""
        period = task.get("period", "afternoon")
        if period in self.daily_schedule:
            self.daily_schedule[period].append({
                "time": task.get("time", "12:00"),
                "task": task.get("task", "New task")
            })

    def _reschedule_task(self, task_update: Dict[str, str]) -> None:
        """Reschedule a specific task."""
        task_name = task_update.get("task_name")
        new_time = task_update.get("new_time")
        
        if not task_name or not new_time:
            return
        
        for period in self.daily_schedule:
            for task in self.daily_schedule[period]:
                if task_name.lower() in task["task"].lower():
                    task["time"] = new_time
                    break

    def get_schedule_summary(self) -> str:
        """Get a formatted summary of the daily schedule."""
        if not self.daily_schedule:
            self.generate_daily_schedule()
        
        summary = "Daily Schedule Summary\n" + "=" * 50 + "\n\n"
        
        for period, tasks in self.daily_schedule.items():
            summary += f"{period.upper()}\n{'-' * 20}\n"
            for task in tasks:
                summary += f"  {task['time']} - {task['task']}\n"
            summary += "\n"
        
        return summary
