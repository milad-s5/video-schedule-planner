from datetime import datetime, timedelta
from models.video import Video

class VideoScheduler:    
    
    @staticmethod
    def schedule_videos(videos, interval_type, time_per_interval):
        schedule = {}
        current_interval_start = datetime.today()
        current_total = 0
        interval_videos = []

        for video in videos:
            if current_total + video.duration <= time_per_interval:
                interval_videos.append(video)
                current_total += video.duration
            else:
                schedule[current_interval_start.strftime("%Y-%m-%d")] = interval_videos
                current_interval_start = VideoScheduler.get_next_interval(interval_type, current_interval_start)
                interval_videos = [video]
                current_total = video.duration

        if interval_videos:
            schedule[current_interval_start.strftime("%Y-%m-%d")] = interval_videos

        return schedule

    @staticmethod
    def get_next_interval(interval_type, current_date):
        if interval_type == 'daily':
            return current_date + timedelta(days=1)
        elif interval_type == 'weekly':
            return current_date + timedelta(weeks=1)
        elif interval_type == 'monthly':
            return current_date + timedelta(weeks=4)  # Approximate month
        return current_date
