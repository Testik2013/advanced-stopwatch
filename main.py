import customtkinter as ctk
import time

ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("blue")

class StopwatchApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Stopwatch")
        self.geometry("400x500")
        self.resizable(False, False)

        # Timer logic
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.laps = []

        # UI Elements
        self.timer_label = ctk.CTkLabel(self, text="00:00:00.00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = ctk.CTkButton(self, text="Start", command=self.toggle_timer)
        self.start_button.pack(pady=10)

        self.lap_button = ctk.CTkButton(self, text="Lap", command=self.record_lap)
        self.lap_button.pack(pady=5)

        self.reset_button = ctk.CTkButton(self, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

        self.lap_frame = ctk.CTkScrollableFrame(self, width=350, height=250)
        self.lap_frame.pack(pady=10)

        self.lap_labels = []

        self.update_timer()

    def toggle_timer(self):
        if self.running:
            self.running = False
            self.start_button.configure(text="Start")
        else:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_button.configure(text="Pause")
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.elapsed_time = 0
        self.timer_label.configure(text="00:00:00.00")
        self.start_button.configure(text="Start")
        for label in self.lap_labels:
            label.destroy()
        self.lap_labels.clear()
        self.laps.clear()

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            formatted_time = self.format_time(self.elapsed_time)
            self.timer_label.configure(text=formatted_time)
        self.after(50, self.update_timer)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hrs, mins = divmod(mins, 60)
        millis = int((secs - int(secs)) * 100)
        return f"{int(hrs):02}:{int(mins):02}:{int(secs)%60:02}.{millis:02}"

    def record_lap(self):
        if self.running:
            lap_time = self.format_time(self.elapsed_time)
            self.laps.append(lap_time)
            label = ctk.CTkLabel(self.lap_frame, text=f"Lap {len(self.laps)} - {lap_time}", font=("Helvetica", 14))
            label.pack(anchor='w', padx=10)
            self.lap_labels.append(label)

if __name__ == "__main__":
    app = StopwatchApp()
    app.mainloop()