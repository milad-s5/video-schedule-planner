# Video Schedule Planner

A Python tool that helps you schedule video content for efficient learning or entertainment. Customize your schedule with flexible intervals (daily, weekly, or monthly) and set a time limit per interval (e.g., 1 hour, 2 hours).

## Features:
- **Customizable intervals**: Choose from daily, weekly, or monthly schedules.
- **Flexible time per interval**: Set how much time you want to dedicate to video watching per interval (in seconds).
- **Media Info Extraction**: Automatically extracts video duration using MediaInfo to help organize your schedule.

## How It Works:
The script organizes your videos into a schedule based on your chosen interval and time per interval settings. It ensures that you are watching an appropriate amount of content each day, week, or month, without exceeding your desired time.

## Configuration:
To configure your schedule, modify the settings in `main.py`:

1. **Set Interval Type**: Choose between `'daily'`, `'weekly'`, or `'monthly'`.
2. **Set Time Per Interval**: Choose how long you want to watch content each interval (in seconds):
    - Example: 3600 seconds = 1 hour.
    - Example: 7200 seconds = 2 hours.
    - Example: 10800 seconds = 3 hours.

```python
# Configuration example:
interval_type = 'daily'  # Options: 'daily', 'weekly', 'monthly'
time_per_interval = 3600  # Duration of each interval in seconds (e.g., 1 hour = 3600)
