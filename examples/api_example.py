#!/usr/bin/env python3
"""
Example script demonstrating how to use the AICoach API programmatically
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stardom_flow import AICoach


def main():
    """Demonstrate AICoach functionality."""
    print("=" * 60)
    print("Key-To-Productivity API Example")
    print("=" * 60)
    print()
    
    # Initialize the AI Coach
    print("1. Initializing AI Coach...")
    coach = AICoach()
    print("   ✓ AI Coach initialized\n")
    
    # Learn user habits
    print("2. Learning user habits...")
    coach.learn_user_habits({
        "name": "Alice Smith",
        "occupation": "Software Engineer",
        "goals": ["improve focus", "better work-life balance"],
        "preferences": {
            "wake_time": "06:30",
            "sleep_time": "22:30",
            "work_hours": 8
        }
    })
    print(f"   ✓ Learned habits for: {coach.user_data['name']}")
    print(f"   ✓ Wake time: {coach.preferences['wake_time']}")
    print(f"   ✓ Sleep time: {coach.preferences['sleep_time']}\n")
    
    # Generate daily schedule
    print("3. Generating daily schedule...")
    schedule = coach.generate_daily_schedule()
    print(f"   ✓ Schedule created with {len(schedule)} periods\n")
    
    # Display schedule summary
    print("4. Schedule Summary:")
    print("-" * 60)
    print(coach.get_schedule_summary())
    
    # Set reminders
    print("5. Setting reminders...")
    reminders = coach.set_reminders()
    print(f"   ✓ {len(reminders)} reminders set\n")
    
    # Demonstrate schedule adjustment - Add a task
    print("6. Adjusting schedule - Adding a task...")
    coach.adjust_schedule({
        "add_tasks": [{
            "period": "afternoon",
            "time": "16:30",
            "task": "Team standup meeting"
        }]
    })
    print("   ✓ Added 'Team standup meeting' at 16:30\n")
    
    # Demonstrate schedule adjustment - Reschedule a task
    print("7. Adjusting schedule - Rescheduling lunch...")
    coach.adjust_schedule({
        "reschedule": [{
            "task_name": "Lunch",
            "new_time": "12:30"
        }]
    })
    print("   ✓ Lunch rescheduled to 12:30\n")
    
    # Display updated schedule
    print("8. Updated Schedule Summary:")
    print("-" * 60)
    print(coach.get_schedule_summary())
    
    print("=" * 60)
    print("Example completed successfully! 🚀")
    print("=" * 60)


if __name__ == "__main__":
    main()
