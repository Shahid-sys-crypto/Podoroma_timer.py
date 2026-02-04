# 🍅 Podoroma Timer (Python + Tkinter)

A simple **Pomodoro Timer desktop application** built using **Python** and **Tkinter**.  
This app helps improve focus and productivity by alternating between work sessions and breaks.

---

## ✨ Features

- ⏱️ **25-minute work sessions**
- ☕ **5-minute short breaks**
- 💤 **15-minute long break after 8 sessions**
- 🎨 **Color-coded session status**
  - Green → Work
  - Red → Short Break
  - Blue → Long Break
- 🔁 **Start and Reset buttons**
- 🖥️ **Minimal GUI built with Tkinter**

---

## 📁 Project Structure


---

## 🛠️ Requirements

- Python **3.x**
- Tkinter (included with standard Python installation)

Check Python version:

---

## ▶️ How to Run

1. Download or clone the project
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the application:


---

## 🧠 How It Works

### Session Logic

- **Even session count** → Work session (25 minutes)
- **Odd session count** → Short break (5 minutes)
- **Every 8th session** → Long break (15 minutes)

### Timer Mechanism

- Uses `window.after()` for countdown updates
- Automatically switches to the next session when the timer ends

---

## 🔘 Button Functions

- **Start**  
  Starts the timer according to the current session type

- **Reset**  
  Resets:
  - Timer to `25:00`
  - Session counter to `0`
  - Status label to `Start`

---

## 🧩 Technologies Used

- Python
- Tkinter (GUI library)

---

## 🚀 Future Enhancements

- Sound notification when session ends
- Pause / Resume button
- Custom session durations
- Session counter display
- Improved UI design

---

## 👤 Author

**Shahid Farhan**  
Beginner-friendly Python GUI project using Tkinter.
