from config import INTERVAL_TYPE, TIME_PER_INTERVAL
from services.video_loader import VideoLoader
from services.scheduler import VideoScheduler
from utils.formatter import Formatter
from utils.file_dialog import FileDialog

def main():
    course_path = FileDialog.select_directory()
    if not course_path:
        print("No directory selected. Exiting.")
        return

    videos = VideoLoader.load_videos(course_path)
    schedule = VideoScheduler.schedule_videos(videos, INTERVAL_TYPE, TIME_PER_INTERVAL)

    Formatter.display_schedule(schedule)
    Formatter.save_schedule(schedule, course_path)

if __name__ == "__main__":
    main()
