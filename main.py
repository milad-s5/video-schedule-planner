import os
import sys
from pymediainfo import MediaInfo
from datetime import datetime, timedelta
from tabulate import tabulate

# Path to your course folder (Modify this)
course_path = r"C:\\path\\to\\your\\course"

# Configuration settings
interval_type = 'daily'  # Options: 'daily', 'weekly', or 'monthly'
time_per_interval = 3600  # Duration of each interval in seconds (e.g., 1 hour = 3600)

print(f"Interval Type: {interval_type}")
print(f"Time Per Interval: {time_per_interval/60} minutes")

if not os.path.exists(course_path):
    print(f"Error: The specified course path '{course_path}' does not exist.")
    sys.exit(1)

def get_video_duration(video_path):
    try:
        media_info = MediaInfo.parse(video_path)
        for track in media_info.tracks:
            if track.track_type == 'Video':
                return track.duration / 1000 
    except Exception as e:
        print(f"Error reading {video_path}: {e}")
        return 0

def format_duration(seconds):
    return str(timedelta(seconds=int(seconds)))

videos = []
for root, _, files in os.walk(course_path):
    for file in sorted(files):  
        if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv')):
            full_path = os.path.abspath(os.path.join(root, file))  
            if os.path.exists(full_path):  
                duration = get_video_duration(full_path)
                videos.append((full_path, duration))
            else:
                print(f"File not found: {full_path}")

def schedule_videos(videos, interval_type, time_per_interval):
    schedule = {}
    current_interval_start = datetime.today()
    current_total = 0
    interval_videos = []

    for video, duration in videos:
        if current_total + duration <= time_per_interval:
            interval_videos.append((video, duration))
            current_total += duration
        else:
            schedule[current_interval_start.strftime("%Y-%m-%d")] = interval_videos
            if interval_type == 'daily':
                current_interval_start += timedelta(days=1)
            elif interval_type == 'weekly':
                current_interval_start += timedelta(weeks=1)
            elif interval_type == 'monthly':
                current_interval_start += timedelta(weeks=4)
            interval_videos = [(video, duration)]
            current_total = duration

    if interval_videos:
        schedule[current_interval_start.strftime("%Y-%m-%d")] = interval_videos

    return schedule

schedule = schedule_videos(videos, interval_type, time_per_interval)

for interval, vids in schedule.items():
    table_data = [(os.path.basename(vid), format_duration(duration)) for vid, duration in vids]
    print(f"\n{interval}:")
    print(tabulate(table_data, headers=["Video Name", "Duration"], tablefmt="grid"))
