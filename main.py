from config import COURSE_PATH, INTERVAL_TYPE, TIME_PER_INTERVAL
from services.video_loader import VideoLoader
from services.scheduler import VideoScheduler
from utils.formatter import Formatter

def main():
    videos = VideoLoader.load_videos(COURSE_PATH)
    schedule = VideoScheduler.schedule_videos(videos, INTERVAL_TYPE, TIME_PER_INTERVAL)

    Formatter.display_schedule(schedule)

if __name__ == "__main__":
    main()
