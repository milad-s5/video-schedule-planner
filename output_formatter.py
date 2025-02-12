from datetime import timedelta
from tabulate import tabulate
import os

class OutputFormatter:
    @staticmethod
    def format_duration(seconds):
        return str(timedelta(seconds=int(seconds)))

    @staticmethod
    def display_schedule(schedule):
        for interval, videos in schedule.items():
            table_data = [(os.path.basename(video.file_path), OutputFormatter.format_duration(video.duration)) for video in videos]
            print(f"\n{interval}:")
            print(tabulate(table_data, headers=["Video Name", "Duration"], tablefmt="grid"))
