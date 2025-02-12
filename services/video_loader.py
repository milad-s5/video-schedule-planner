import os
from pymediainfo import MediaInfo
from models.video import Video
from utils.file_checker import FileChecker

class VideoLoader:
    
    @staticmethod
    def get_video_duration(video_path):
        try:
            media_info = MediaInfo.parse(video_path)
            for track in media_info.tracks:
                if track.track_type == 'Video':
                    return track.duration / 1000  # Convert to seconds
        except Exception as e:
            print(f"Error reading {video_path}: {e}")
        return 0

    @staticmethod
    def load_videos(course_path):
        FileChecker.check_course_path(course_path)

        videos = []
        for root, _, files in os.walk(course_path):
            for file in sorted(files):
                if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv')):
                    full_path = os.path.abspath(os.path.join(root, file))
                    if os.path.exists(full_path):
                        duration = VideoLoader.get_video_duration(full_path)
                        videos.append(Video(full_path, duration))
                    else:
                        print(f"File not found: {full_path}")
        return videos
