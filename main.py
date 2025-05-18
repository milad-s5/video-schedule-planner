from config import INTERVAL_TYPE, TIME_PER_INTERVAL
from services.video_loader import VideoLoader
from services.scheduler import VideoScheduler
from gui.schedule_viewer import ScheduleViewer
from utils.file_dialog import FileDialog
from utils.formatter import Formatter

def main():
    course_path = FileDialog.select_directory()
    if not course_path:
        print("No directory selected. Exiting.")
        return

    videos = VideoLoader.load_videos(course_path)
    schedule = VideoScheduler.schedule_videos(videos, INTERVAL_TYPE, TIME_PER_INTERVAL)

    # Display the schedule
    ScheduleViewer.display_schedule(schedule)
    
    # Save the schedule
    Formatter.save_schedule(schedule, course_path)

if __name__ == "__main__":
    main()
