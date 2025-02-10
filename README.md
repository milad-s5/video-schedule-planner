# Video Schedule Planner

A Python tool that helps you schedule video content for efficient learning or entertainment. Customize your schedule with flexible intervals (daily, weekly, or monthly) and set a time limit per interval (e.g., 1 hour, 2 hours).

## Features:
- **Customizable intervals**: Choose from daily, weekly, or monthly schedules.
- **Flexible time per interval**: Set how much time you want to dedicate to video watching per interval (in seconds).
- **Media Info Extraction**: Automatically extracts video duration using MediaInfo to help organize your schedule.

## How It Works:
The script organizes your videos into a schedule based on your chosen interval and time per interval settings. It ensures that you are watching an appropriate amount of content each day, week, or month, without exceeding your desired time.

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
  - 001 Introduction to Reinforcement Learning.mp4
  - 002 Understanding Markov Decision Processes.mp4
  - 003 Key Concepts: States, Actions, and Rewards.mp4
  - 004 The Exploration-Exploitation Dilemma.mp4
  - 005 Value Iteration and Policy Iteration.mp4
  - 006 Dynamic Programming in RL.mp4
  - 007 Q-Learning: A Model-Free Method.mp4

2025-02-11:
  - 008 Deep Q-Learning: Neural Networks in RL.mp4
  - 009 Policy Gradient Methods.mp4
  - 010 Actor-Critic Algorithms.mp4
  - 011 Introduction to Multi-Agent Reinforcement Learning.mp4
  - 012 Inverse Reinforcement Learning.mp4
  - 013 RL in Real-World Applications.mp4
  - 014 Challenges and Future of RL Research.mp4
```

## How to Run
1. Install required dependencies:
```bash
pip install -r requirements.txt
```
2. Modify the course_path variable in main.py to the location of your video files.

3. Configure the interval type ('daily', 'weekly', or 'monthly') and time per interval (in seconds).

4. Run the script
```bash
python main.py
```

## Customization
* You can modify the time per interval to fit your personal schedule.
* The script supports video files with extensions like .mp4, .mkv, .avi, .mov, .flv, and will automatically calculate the duration of each video.
* The script generates a schedule for watching the videos in sequence, ensuring you stay within the desired time frame for each interval.