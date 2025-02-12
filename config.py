import os
import sys

# Path to your course folder (Modify this)
COURSE_PATH = r"C:\\path\\to\\your\\course"

# Configuration settings
INTERVAL_TYPE = 'daily'  # Options: 'daily', 'weekly', or 'monthly'
TIME_PER_INTERVAL = 3600  # Duration of each interval in seconds (e.g., 1 hour = 3600)

print(f"Interval Type: {INTERVAL_TYPE}")
print(f"Time Per Interval: {TIME_PER_INTERVAL / 60} minutes")

if not os.path.exists(COURSE_PATH):
    print(f"Error: The specified course path '{COURSE_PATH}' does not exist.")
    sys.exit(1)
