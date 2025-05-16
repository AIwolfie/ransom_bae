import tkinter as tk
from tkinter import messagebox
import time
import threading
import keyboard  # pip install keyboard

# Message
RANSOM_NOTE = """
😈 Oops! Your college project files have been encrypted by RANSOM-BAE 😈

To get them back, bring me a cold coffee ☕ from the canteen.

You have {minutes} minutes and {seconds} seconds before your GPA drops to 0.0!
"""

TIMER_SECONDS = 300  # 5 mins
SECRET_EXIT_COMBO = "<Control-q>"

class RansomBaeApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

        # Block system close keys
        self.root.protocol("WM_DELETE_WINDOW", self.block_action)
        self.root.bind_all("<Alt-F4>", self.block_warning)
        self.root.bind_all("<Escape>", self.block_warning)
        self.root.bind_all("<F11>", self.block_warning)
        self.root.bind_all("<Control-w>", self.block_warning)
        self.root.bind_all("<Control-q>", self.exit_program)
        self.root.bind_all("<Control-Q>", self.exit_program)

        # Keep it always on top and focused
        threading.Thread(target=self.force_focus, daemon=True).start()
        # Try to block Windows key
        threading.Thread(target=self.block_windows_key, daemon=True).start()

        self.time_left = TIMER_SECONDS

        self.message_label = tk.Label(
            root,
            text="",
            font=("Courier", 18),
            fg="lime",
            bg="black",
            justify="center",
            wraplength=1000,
        )
        self.message_label.pack(pady=50)

        self.timer_label = tk.Label(
            root,
            text="",
            font=("Courier", 24, "bold"),
            fg="red",
            bg="black"
        )
        self.timer_label.pack()

        self.button_frame = tk.Frame(root, bg="black")
        self.button_frame.pack(pady=40)

        self.pay_button = tk.Button(
            self.button_frame,
            text="💸 Pay Ransom",
            font=("Courier", 16),
            command=self.pay_ransom,
            bg="gray20",
            fg="white"
        )
        self.pay_button.grid(row=0, column=0, padx=20)

        self.hack_button = tk.Button(
            self.button_frame,
            text="💻 Try to Hack Back",
            font=("Courier", 16),
            command=self.try_hack_back,
            bg="gray20",
            fg="white"
        )
        self.hack_button.grid(row=0, column=1, padx=20)

        self.give_up_button = tk.Button(
            self.button_frame,
            text="😵 Give Up",
            font=("Courier", 16),
            command=self.give_up,
            bg="gray20",
            fg="white"
        )
        self.give_up_button.grid(row=0, column=2, padx=20)

        self.update_message()
        threading.Thread(target=self.countdown_timer, daemon=True).start()

    def force_focus(self):
        while True:
            time.sleep(0.4)
            try:
                self.root.attributes("-topmost", True)
                self.root.focus_force()
            except:
                pass

    def block_windows_key(self):
        try:
            keyboard.block_key('windows')
            keyboard.block_key('left windows')
            keyboard.block_key('right windows')
        except:
            pass

    def update_message(self):
        minutes, seconds = divmod(self.time_left, 60)
        self.message_label.config(text=RANSOM_NOTE.format(minutes=minutes, seconds=seconds))

    def countdown_timer(self):
        while self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.update_message()
            self.timer_label.config(text=f"⏳ Time Left: {self.time_left} seconds")
        self.time_up()

    def pay_ransom(self):
        messagebox.showinfo("Payment", "Thank you for the coffee! 😂\nDecrypting files... Just kidding!")

    def try_hack_back(self):
        messagebox.showwarning("Hack Failed", "Access Denied! Stick to your classes, hacker-wannabe.")

    def give_up(self):
        messagebox.showinfo("Game Over", "RIP GPA 💀\nSee you next semester.")

    def time_up(self):
        messagebox.showerror("Time's Up!", "GPA has been sent to 0.0!\nBetter luck next semester.")

    def exit_program(self, event=None):
        self.root.destroy()

    def block_action(self, event=None):
        return "break"

    def block_warning(self, event=None):
        messagebox.showwarning("No Escape", "Even Alt+F4 can't save your GPA now 😈")
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    app = RansomBaeApp(root)
    root.mainloop()
