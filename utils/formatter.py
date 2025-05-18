from datetime import timedelta
import os
from tabulate import tabulate
import csv

class Formatter:
    
    @staticmethod
    def format_duration(seconds):
        return str(timedelta(seconds=int(seconds)))

    @staticmethod
    def display_schedule(schedule):
        Formatter._print_or_save_schedule(schedule)

    @staticmethod
    def save_schedule(schedule, directory):
        # Save as text file
        txt_output_file = os.path.join(directory, "schedule.txt")
        Formatter._print_or_save_schedule(schedule, txt_output_file)
        print(f"Schedule saved to {txt_output_file}")
        
        # Save as CSV file
        csv_output_file = os.path.join(directory, "schedule.csv")
        Formatter._save_schedule_csv(schedule, csv_output_file)
        print(f"Schedule saved to {csv_output_file}")

    @staticmethod
    def _save_schedule_csv(schedule, output_file):
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Interval', 'Video Name', 'Duration', 'Total Interval Time'])
            
            for interval, videos in schedule.items():
                total_time = sum(video.duration for video in videos)
                formatted_total_time = Formatter.format_duration(total_time)
                
                for video in videos:
                    writer.writerow([
                        interval,
                        os.path.basename(video.file_path),
                        Formatter.format_duration(video.duration),
                        formatted_total_time
                    ])

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
