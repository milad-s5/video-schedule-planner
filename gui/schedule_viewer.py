import tkinter as tk
from tkinter import ttk
from datetime import timedelta

class ScheduleViewer:
    @staticmethod
    def format_duration(seconds):
        return str(timedelta(seconds=int(seconds)))

    @staticmethod
    def display_schedule(schedule):
        root = tk.Tk()
        root.title("Video Schedule")

        root.state('zoomed')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.configure("Treeview", font=("Helvetica", 10), rowheight=25)

        frame = ttk.Frame(root)
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        tree = ttk.Treeview(frame, columns=("Video Name", "Duration"), show='headings')
        tree.heading("Video Name", text="Video Name")
        tree.heading("Duration", text="Duration")

        for interval, videos in schedule.items():
            total_duration = sum(video.duration for video in videos)
            tree.insert("", "end", values=(f"{interval} (Total: {ScheduleViewer.format_duration(total_duration)})", ""), tags=("interval",))
            for video in videos:
                tree.insert("", "end", values=(video.file_path, ScheduleViewer.format_duration(video.duration)))

        tree.tag_configure("interval", background="#f0f0f0", font=("Helvetica", 10, "bold"))

        tree.pack(side="left", expand=True, fill='both')

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        root.protocol("WM_DELETE_WINDOW", root.quit)

        root.mainloop()
