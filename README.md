# Video Schedule Planner

A Python tool that helps you schedule video content for efficient learning or entertainment. Customize your schedule with flexible intervals (daily, weekly, or monthly) and set a time limit per interval (e.g., 1 hour, 2 hours). The schedule is displayed in a structured table format for better readability.

## Features:
- **Customizable intervals**: Choose from daily, weekly, or monthly schedules.
- **Flexible time per interval**: Set how much time you want to dedicate to video watching per interval (in seconds).
- **Media Info Extraction**: Automatically extracts video duration using MediaInfo to help organize your schedule.
- **Formatted Output**: Displays the schedule in a structured table format using `tabulate` for better readability.

## Installation

### Linux
1. Install system dependencies:
```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3-pip python3-tk mediainfo

# For Fedora
sudo dnf install -y python3-pip python3-tkinter mediainfo

# For Arch Linux
sudo pacman -S python-pip tk mediainfo
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Windows
1. Install Python 3.x from [python.org](https://www.python.org/downloads/)
2. Install MediaInfo from [mediaarea.net](https://mediaarea.net/en/MediaInfo/Download/Windows)
3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Linux
1. Make the executable file executable:
```bash
chmod +x dist/video-schedule-planner
```

2. Run the application:
```bash
./dist/video-schedule-planner
```

### Windows
Simply double-click the `video-schedule-planner.exe` file in the `dist` directory.

## Building from Source

1. Install build dependencies:
```bash
pip install -r requirements.txt
```

2. Create icons:
```bash
python create_icon.py
```

3. Build the executable:
```bash
python build.py
```

The executable will be created in the `dist` directory.

## Usage
1. Run the application
2. Select the directory containing your video files
3. The application will:
   - Scan all video files in the directory
   - Create a schedule based on your configured interval type and time per interval
   - Display the schedule in a GUI window
   - Save the schedule as both text and CSV files in the same directory

## Configuration
To configure your schedule, modify the settings in `config.py`:

1. **Set Interval Type**: Choose between `'daily'`, `'weekly'`, or `'monthly'`.
2. **Set Time Per Interval**: Choose how long you want to watch content each interval (in seconds):
    - Example: 3600 seconds = 1 hour
    - Example: 7200 seconds = 2 hours
    - Example: 10800 seconds = 3 hours

## Troubleshooting

### Linux
If you encounter any issues:
1. Make sure MediaInfo is installed: `mediainfo --version`
2. Check if tkinter is installed: `python3 -c "import tkinter; tkinter._test()"`
3. Ensure the executable has proper permissions: `chmod +x video-schedule-planner`

### Windows
If you encounter any issues:
1. Make sure MediaInfo is installed and in your system PATH
2. Verify Python is installed and in your system PATH
3. Try running the application from the command line to see any error messages

## How It Works:
The script organizes your videos into a schedule based on your chosen interval and time per interval settings. It ensures that you are watching an appropriate amount of content each day, week, or month, without exceeding your desired time. The schedule is displayed as a neatly formatted table.

## Configuration:
To configure your schedule, modify the settings in `main.py`:

1. **Set Interval Type**: Choose between `'daily'`, `'weekly'`, or `'monthly'`.
2. **Set Time Per Interval**: Choose how long you want to watch content each interval (in seconds):
    - Example: 3600 seconds = 1 hour.
    - Example: 7200 seconds = 2 hours.
    - Example: 10800 seconds = 3 hours.

```python
# Configuration example:
interval_type = 'daily'  # Options: 'daily', 'weekly', 'monthly'
time_per_interval = 3600  # Duration of each interval in seconds (e.g., 1 hour = 3600)
```

## Example Usage
```python
[Running] python -u "f:\Projects\video-schedule-planner\main.py"
Interval Type: daily
Time Per Interval: 60.0 minutes

2025-02-10:
+--------------------------------------+------------+
| Video Name                           | Duration   |
+--------------------------------------+------------+
| 001 Introduction to RL.mp4           | 00:12:34   |
| 002 Understanding MDPs.mp4           | 00:15:20   |
| 003 Key Concepts.mp4                 | 00:09:45   |
| 004 Exploration-Exploitation.mp4     | 00:14:10   |
| 005 Value Iteration.mp4              | 00:18:30   |
+--------------------------------------+------------+

2025-02-11:
+--------------------------------------+------------+
| Video Name                           | Duration   |
+--------------------------------------+------------+
| 006 Deep Q-Learning.mp4              | 00:20:15   |
| 007 Policy Gradient Methods.mp4      | 00:16:40   |
| 008 Actor-Critic Algorithms.mp4      | 00:13:55   |
| 009 Multi-Agent RL.mp4               | 00:11:50   |
+--------------------------------------+------------+
```

## How to Run
1. Install required dependencies:
```bash
pip install -r requirements.txt
```
2. Modify the `course_path` variable in `main.py` to the location of your video files.

3. Configure the interval type ('daily', 'weekly', or 'monthly') and time per interval (in seconds).

4. Run the script:
```bash
python main.py
```

## Customization
* You can modify the time per interval to fit your personal schedule.
* The script supports video files with extensions like `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv` and will automatically calculate the duration of each video.
* The script generates a schedule for watching the videos in sequence, ensuring you stay within the desired time frame for each interval.
* The output is displayed as a formatted table for clear visualization of the schedule.

