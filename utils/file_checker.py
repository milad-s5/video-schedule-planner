import os
import sys

class FileChecker:

    @staticmethod
    def check_course_path(course_path):
        if not os.path.exists(course_path):
            print(f"Error: The specified course path '{course_path}' does not exist.")
            sys.exit(1)
