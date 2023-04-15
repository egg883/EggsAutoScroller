import pyautogui
import time
import tkinter as tk
from tkinter.ttk import Style

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.scroll_speed = 0.65
        self.scroll_distance = 120
        self.scroll_on = False
        self.bg_color = "#282C34"
        self.fg_color = "#ABB2BF"
        self.button_bg_color = "#3E4451"
        self.button_fg_color = "#FFFFFF"
        self.start_time = time.time()
        self.create_widgets()
        
        self.master.iconbitmap("egg.ico")
        self.master.title("Eggs Auto Scroller")
        self.master.resizable(False, False)
        self.master.configure(background=self.bg_color)

        style = Style()
        style.theme_use("clam")
        style.configure("TButton", background=self.button_bg_color, foreground=self.button_fg_color)
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color)

    def create_widgets(self):
        self.scroll_button = tk.Button(self.master, text="Toggle Scrolling", command=self.toggle_scroll)
        self.scroll_button.pack(pady=20)
        self.made_by_label = tk.Label(self.master, text="Made by Egg883")
        self.made_by_label.pack(side="right", padx=9, pady=9, anchor="se")

        self.master.geometry("300x130+500+300")

    def toggle_scroll(self, event=None):
        self.scroll_on = not self.scroll_on
        if self.scroll_on:
            self.scroll_button.config(text="Stop Scrolling")
            self.scroll()
        else:
            self.scroll_button.config(text="Toggle Scrolling")
            self.master.after_cancel(self.master.after_id)

    def scroll(self):
        start_pos = pyautogui.position()
        for i in range(10):
            pyautogui.scroll(-self.scroll_distance, x=start_pos.x, y=start_pos.y)
            time.sleep(self.scroll_speed)
            if not self.scroll_on:
                break
        if self.scroll_on:
            self.master.after_id = self.master.after(10, self.scroll)

root = tk.Tk()
app = App(master=root)
app.mainloop()