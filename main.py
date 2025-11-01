#!/usr/bin/env python3
"""
Key-To-Productivity Application
Main entry point for the productivity enhancement application
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from stardom_flow import initialize_stardom_flow


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print(" " * 15 + "KEY TO PRODUCTIVITY")
    print(" " * 15 + "Stardom Flow AI Coach")
    print("=" * 60)
    print("\nMenu Options:")
    print("  1. Generate Daily Schedule")
    print("  2. Set Reminders")
    print("  3. View Schedule Summary")
    print("  4. Adjust Schedule")
    print("  5. Update Preferences")
    print("  6. Learn User Habits")
    print("  7. Exit")
    print("-" * 60)


def get_user_choice():
    """Get user menu choice."""
    try:
        choice = input("\nEnter your choice (1-7): ").strip()
        return choice
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting application...")
        return "7"


def update_preferences(coach):
    """Update user preferences."""
    print("\n--- Update Preferences ---")
    print("Current preferences:")
    for key, value in coach.preferences.items():
        print(f"  {key}: {value}")
    
    print("\nEnter new values (press Enter to keep current):")
    
    wake_time = input(f"Wake time [{coach.preferences['wake_time']}]: ").strip()
    if wake_time:
        coach.preferences['wake_time'] = wake_time
    
    sleep_time = input(f"Sleep time [{coach.preferences['sleep_time']}]: ").strip()
    if sleep_time:
        coach.preferences['sleep_time'] = sleep_time
    
    work_hours = input(f"Work hours [{coach.preferences['work_hours']}]: ").strip()
    if work_hours:
        try:
            coach.preferences['work_hours'] = int(work_hours)
        except ValueError:
            print("Invalid number for work hours, keeping current value.")
    
    print("\nPreferences updated successfully!")


def learn_habits(coach):
    """Learn user habits interactively."""
    print("\n--- Learn User Habits ---")
    print("Enter information about your habits:")
    
    name = input("Your name: ").strip()
    occupation = input("Your occupation: ").strip()
    goals = input("Your main goals (comma-separated): ").strip()
    
    data = {
        "name": name,
        "occupation": occupation,
        "goals": [g.strip() for g in goals.split(",")] if goals else []
    }
    
    coach.learn_user_habits(data)
    print("\nHabits learned successfully!")
    print(f"Stored data: {coach.user_data}")


def adjust_schedule_interactive(coach):
    """Adjust schedule interactively."""
    print("\n--- Adjust Schedule ---")
    print("1. Skip a task")
    print("2. Add a new task")
    print("3. Reschedule a task")
    print("4. Cancel")
    
    choice = input("\nYour choice (1-4): ").strip()
    
    if choice == "1":
        task_name = input("Enter task name to skip: ").strip()
        coach.adjust_schedule({"skip_tasks": [task_name]})
        print(f"Task '{task_name}' removed from schedule.")
    
    elif choice == "2":
        task_name = input("Enter task name: ").strip()
        task_time = input("Enter task time (HH:MM): ").strip()
        period = input("Enter period (morning/afternoon/evening): ").strip().lower()
        
        coach.adjust_schedule({
            "add_tasks": [{
                "task": task_name,
                "time": task_time,
                "period": period if period in ["morning", "afternoon", "evening"] else "afternoon"
            }]
        })
        print(f"Task '{task_name}' added to schedule.")
    
    elif choice == "3":
        task_name = input("Enter task name to reschedule: ").strip()
        new_time = input("Enter new time (HH:MM): ").strip()
        
        coach.adjust_schedule({
            "reschedule": [{
                "task_name": task_name,
                "new_time": new_time
            }]
        })
        print(f"Task '{task_name}' rescheduled to {new_time}.")
    
    else:
        print("Cancelled.")


def main():
    """Main application loop."""
    print("\nInitializing Key-To-Productivity Application...")
    coach = initialize_stardom_flow()
    print("AI Coach initialized successfully!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            print("\n--- Generating Daily Schedule ---")
            schedule = coach.generate_daily_schedule()
            print("\nSchedule generated successfully!")
            print(f"\nYou have {len(schedule)} time periods scheduled:")
            for period in schedule:
                print(f"  - {period.capitalize()}")
        
        elif choice == "2":
            print("\n--- Setting Reminders ---")
            reminders = coach.set_reminders()
            print(f"\n{len(reminders)} reminders set:")
            for reminder in reminders:
                print(f"  ⏰ {reminder}")
        
        elif choice == "3":
            print("\n")
            print(coach.get_schedule_summary())
        
        elif choice == "4":
            adjust_schedule_interactive(coach)
        
        elif choice == "5":
            update_preferences(coach)
        
        elif choice == "6":
            learn_habits(coach)
        
        elif choice == "7":
            print("\nThank you for using Key-To-Productivity!")
            print("Stay productive! 🚀\n")
            break
        
        else:
            print("\n⚠️  Invalid choice. Please select 1-7.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
