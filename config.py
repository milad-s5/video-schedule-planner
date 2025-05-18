import os
import sys

# Configuration settings
INTERVAL_TYPE = 'daily'  # Options: 'daily', 'weekly', or 'monthly'
TIME_PER_INTERVAL = 15 * 60  # Duration of each interval in seconds (e.g., 1 hour = 3600)

print(f"Interval Type: {INTERVAL_TYPE}")
print(f"Time Per Interval: {TIME_PER_INTERVAL / 60} minutes")
