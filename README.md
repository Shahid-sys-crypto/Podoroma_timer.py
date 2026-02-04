🍅 Podoroma Timer (Python + Tkinter)

A simple Pomodoro Timer desktop app built using Python and Tkinter.
It helps you stay focused using work sessions and short/long breaks.

✨ Features

⏱️ 25-minute work sessions

☕ 5-minute short breaks

💤 15-minute long break after 8 sessions

🎨 Color-coded status:

Green → Work

Red → Short Break

Blue → Long Break

🔁 Start & Reset buttons

🖥️ Simple GUI using Tkinter

📁 Project Structure
podoroma_timer.py
README.md

🛠️ Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

To check Python:

python --version

▶️ How to Run

Clone or download the project

Open terminal / command prompt

Navigate to the project folder

Run the app:

python podoroma_timer.py

🧠 How It Works
Session Logic

Even session count → Work (25 min)

Odd session count → Short break (5 min)

Every 8th session → Long break (15 min)

Countdown

Uses window.after() to update the timer every second

Automatically switches to the next session when time ends

🔘 Buttons

Start → Begins the timer based on current session

Reset → Resets timer to 25:00 and session count to 0

🧩 Technologies Used

Python

Tkinter (GUI)

🚀 Future Improvements (Ideas)

Sound notification when session ends

Pause / Resume button

Custom time settings

Session counter display

👤 Author

Shahid Farhan
Beginner-friendly project for learning Python GUI and timers.
