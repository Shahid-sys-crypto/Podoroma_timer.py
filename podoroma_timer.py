import tkinter as tk
session_count=0
timer_running=False
def countdown(seconds):
    global timer_running
    if seconds>=0:
        mins,secs=divmod(seconds,60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        window.after(1,countdown,seconds-1)
    else:
        timer_running=False
        start_timer()
def start_timer():
    global session_count,timer_running
    if not timer_running:
        timer_running=True
        if session_count % 8==7:
            countdown(15*60)
            status_label.config(text="long break",fg="blue")
        elif session_count % 2 == 0:
            countdown(25*60)
            status_label.config(text="work",fg="green")
        else:
            countdown(5*60)
            status_label.config(text="short break",fg="red")
    session_count+=1
def reset_timer():
    global session_count,timer_running
    session_count=0
    timer_running=False
    timer_label.config(text="25:00",font=("Arial",80))
    status_label.config(text="start",font=("Arial",40))
window=tk.Tk()
window.title("podoroma timer")
window.geometry("500x500")

timer_label=tk.Label(window,text="25:00",font=("Arial",80))
timer_label.pack(pady=20)

status_label=tk.Label(window,text="start",font=("Arial",40))
status_label.pack()

start_button=tk.Button(window,text="start",font=("Arial",32),command=start_timer)
start_button.pack(side="left",padx=10)

reset_button=tk.Button(window,text="reset",font=("Arial",32),command=reset_timer)
reset_button.pack(side="right",padx=10)
window.mainloop()
