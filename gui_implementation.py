from tkinter import *
from tkinter.ttk import *
import sys
import os
import threading
import time
root = Tk()
root.geometry('600x300')

def close_gui():
    time.sleep(6000)  # Wait for 60 seconds
    os._exit(0)  # Close the program

def play_game():
    script_path = r"C:\Users\FLEX\python_files\project_files\NeuroTech X\Dino-Game-main\Dino-Game-main\Dino Game\main.py"
    if os.path.exists(script_path):
        try:
            module_name = os.path.splitext(os.path.basename(script_path))[0]
            script_module = __import__(module_name)
            script_module.main()  
        except Exception as e:
            print(f"Error executing script: {e}")
    else:
        print("Script file not found")
def Read():
    path = r"C:\Users\FLEX\python_files\project_files\NeuroTech X\Dino-Game-main\Dino-Game-main\Dino Game\read__.py"
    if os.path.exists(path):
        try:
            module_name = os.path.splitext(os.path.basename(path))[0]
            script_module = __import__(module_name)
            threading.Thread(target=close_gui).start()
            os._exit(0)
            script_module.main()  
        except Exception as e:
            print(f"Error executing script: {e}")
    else:
        print("Script file not found")

    
style = Style()
style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')
style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

btn = Button(root, text="Let's Play", style='W.TButton', command=play_game)
btn.grid(row=0, column=3, padx=100)
btn2 = Button(root,text="Read !",style='W.TButton',command=Read)
btn2.grid(row=0, column=7, padx=100) 
root.mainloop()
