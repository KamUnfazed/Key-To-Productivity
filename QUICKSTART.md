# Quick Start Guide - Key-To-Productivity

## Installation

```bash
# Clone the repository
git clone https://github.com/KamUnfazed/Key-To-Productivity.git
cd Key-To-Productivity

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
python3 main.py
```

## Basic Usage

### 1. First Time Setup

When you first run the application:

1. Select option **6** (Learn User Habits)
2. Enter your name, occupation, and goals
3. This helps the AI personalize your schedule

### 2. Generate Your Schedule

1. Select option **1** (Generate Daily Schedule)
2. The AI creates a schedule based on your preferences
3. Default schedule includes morning, afternoon, and evening activities

### 3. Set Reminders

1. Select option **2** (Set Reminders)
2. Automatic reminders are created for all your scheduled tasks
3. Each reminder shows the time and task description

### 4. View Your Schedule

1. Select option **3** (View Schedule Summary)
2. See a complete formatted view of your day
3. Organized by morning, afternoon, and evening

### 5. Customize Your Preferences

1. Select option **5** (Update Preferences)
2. Modify:
   - Wake time (default: 07:00)
   - Sleep time (default: 22:00)
   - Work hours (default: 8)
3. Your schedule will adapt to these changes

### 6. Adjust Your Schedule

1. Select option **4** (Adjust Schedule)
2. Choose to:
   - Skip tasks you don't need
   - Add new tasks to your day
   - Reschedule existing tasks to different times

## Example Session

```
Start the app → Learn Habits → Generate Schedule → Set Reminders → View Summary
```

## Tips

- Update your preferences first for a more personalized schedule
- Use the adjust schedule feature to adapt to daily changes
- Set reminders to stay on track throughout the day
- Review your schedule summary at the start of each day

## Command Line Usage

For quick demonstrations:
```bash
# View schedule directly
echo -e "3\n7\n" | python3 main.py

# Generate and view
echo -e "1\n\n3\n\n7\n" | python3 main.py
```

## Programmatic Usage

See `examples/api_example.py` for using the AICoach class directly in your code.

```python
from stardom_flow import AICoach

coach = AICoach()
coach.generate_daily_schedule()
print(coach.get_schedule_summary())
```

## Support

For issues or questions, please open an issue on GitHub:
https://github.com/KamUnfazed/Key-To-Productivity/issues
