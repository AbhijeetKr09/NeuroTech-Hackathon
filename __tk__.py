import tkinter as tk
from threading import Timer

class DataInputGUI:
    def _init_(self, master):
        self.master = master
        master.title("Data Input GUI")

        self.label = tk.Label(master, text="Enter some data:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.start_timer)
        self.submit_button.pack(pady=10)

    def start_timer(self):
        data = self.entry.get()
        if data:
            self.label.config(text=f"Data submitted: {data}")
            self.submit_button.config(state=tk.DISABLED)  # Disable the submit button
            self.timer = Timer(60, self.close_gui)
            self.timer.start()

    def close_gui(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    gui = DataInputGUI(root)
    root.mainloop()

if __name__ == "_main_":
    main()