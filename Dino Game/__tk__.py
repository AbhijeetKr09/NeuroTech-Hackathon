import tkinter as tk

counter = 0
active_counter = False

def count():
    if active_counter:
        global counter
        counter += 1
        label.config(text=counter)
        label.after(1000, count)

def start_stop():
    global active_counter
    if button['text'] == 'Start':
        active_counter = True
        count()
        button.config(text="Stop")
    else:
        active_counter = False
        button.config(text="Start")

root = tk.Tk()
root.title("Counting Seconds")

label = tk.Label(root, fg="green")
label.pack()

button = tk.Button(root, text='Start', width=25, command=start_stop)
button.pack()

stop_button = tk.Button(root, text='Stop', width=25, command=lambda: button.invoke())
stop_button.pack()

root.mainloop()
