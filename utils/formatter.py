from datetime import timedelta
import os
from tabulate import tabulate

class Formatter:
    
    @staticmethod
    def format_duration(seconds):
        return str(timedelta(seconds=int(seconds)))

    @staticmethod
    def display_schedule(schedule):
        for interval, videos in schedule.items():
            total_time = sum(video.duration for video in videos)
            formatted_total_time = Formatter.format_duration(total_time)
            table_data = [(os.path.basename(video.file_path), Formatter.format_duration(video.duration)) for video in videos]
            
            print(f"\n{interval} - Total Time: {formatted_total_time}")
            print(tabulate(table_data, headers=["Video Name", "Duration"], tablefmt="grid"))
