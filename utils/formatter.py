from datetime import timedelta
import os
from tabulate import tabulate

class Formatter:
    
    @staticmethod
    def format_duration(seconds):
        return str(timedelta(seconds=int(seconds)))

    @staticmethod
    def display_schedule(schedule):
        Formatter._print_or_save_schedule(schedule)

    @staticmethod
    def save_schedule(schedule, directory):
        output_file = os.path.join(directory, "schedule.txt")
        Formatter._print_or_save_schedule(schedule, output_file)
        print(f"Schedule saved to {output_file}")

    @staticmethod
    def _print_or_save_schedule(schedule, output_file=None):
        output = []
        for interval, videos in schedule.items():
            total_time = sum(video.duration for video in videos)
            formatted_total_time = Formatter.format_duration(total_time)
            table_data = [(os.path.basename(video.file_path), Formatter.format_duration(video.duration)) for video in videos]
            
            output.append(f"\n{interval} - Total Time: {formatted_total_time}")
            output.append(tabulate(table_data, headers=["Video Name", "Duration"], tablefmt="grid"))
        
        if output_file:
            with open(output_file, "w") as f:
                f.write("\n".join(output))
        else:
            print("\n".join(output))
