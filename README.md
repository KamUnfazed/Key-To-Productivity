# Key-To-Productivity

This repository contains the Key-To-Productivity application, which aims to enhance productivity through various modules, including the Stardom Flow AI module.

## Features

- **AI-Driven Daily Scheduler**: Generate optimized daily schedules based on your preferences
- **Smart Reminders**: Set automatic reminders for all your scheduled tasks
- **Habit Learning**: The AI learns from your habits and preferences to provide personalized schedules
- **Dynamic Schedule Adjustment**: Easily modify your schedule by adding, removing, or rescheduling tasks
- **Customizable Preferences**: Set your wake time, sleep time, work hours, and break intervals

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/KamUnfazed/Key-To-Productivity.git
cd Key-To-Productivity
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install the package:
```bash
pip install -e .
```

## Usage

### Running the Application

Run the main application:
```bash
python3 main.py
```

### Menu Options

The application provides an interactive menu with the following options:

1. **Generate Daily Schedule**: Create a personalized daily schedule based on your preferences
2. **Set Reminders**: Generate reminders for all scheduled tasks
3. **View Schedule Summary**: Display your complete daily schedule in a formatted view
4. **Adjust Schedule**: Modify your schedule by:
   - Skipping tasks
   - Adding new tasks
   - Rescheduling existing tasks
5. **Update Preferences**: Change your wake time, sleep time, and work hours
6. **Learn User Habits**: Input information about yourself for personalized scheduling
7. **Exit**: Close the application

### Example Workflow

```bash
# Start the application
python3 main.py

# Select option 1 to generate a schedule
# Select option 2 to set reminders
# Select option 3 to view your complete schedule
# Select option 5 to update your preferences
# Select option 7 to exit
```

## Project Structure

```
Key-To-Productivity/
├── src/
│   └── stardom_flow/
│       ├── __init__.py          # Module initialization
│       └── ai_coach.py          # AICoach class implementation
├── tests/
│   ├── __init__.py
│   └── test_ai_coach.py         # Unit tests for AICoach
├── main.py                      # Main application entry point
├── setup.py                     # Package setup configuration
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Development

### Running Tests

Run the test suite:
```bash
python3 -m unittest discover tests -v
```

### Using the AICoach Class Programmatically

```python
from stardom_flow import AICoach

# Initialize the coach
coach = AICoach()

# Learn user habits
coach.learn_user_habits({
    "name": "John Doe",
    "occupation": "Developer",
    "preferences": {
        "wake_time": "06:00",
        "sleep_time": "23:00"
    }
})

# Generate a daily schedule
schedule = coach.generate_daily_schedule()

# Set reminders
reminders = coach.set_reminders()

# Get schedule summary
summary = coach.get_schedule_summary()
print(summary)

# Adjust schedule
coach.adjust_schedule({
    "add_tasks": [{
        "period": "afternoon",
        "time": "16:00",
        "task": "Team meeting"
    }]
})
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

KamUnfazed

## Acknowledgments

- Built with Python
- Designed for productivity enthusiasts