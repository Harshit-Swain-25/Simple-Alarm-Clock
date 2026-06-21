# Simple Alarm Clock using Python

A command-line Alarm Clock application built using Python. This project allows users to set alarms either for a specific time or after a chosen number of seconds and notifies them when the alarm time is reached.

The application also supports playing alarm sounds based on the operating system.

## 📌 Project Overview

This project simulates a digital alarm clock in a terminal environment.

Users can choose between setting an alarm for an exact time using a 24-hour format or creating a countdown alarm that triggers after a specified duration.

The application continuously displays the remaining time until the alarm activates.

## 🚀 Features

* Set alarms using a specific time
* Set alarms using a countdown timer
* Real-time countdown display
* Cross-platform alarm support
* Audio notification support
* Graceful interruption handling
* Beginner-friendly implementation

## 🛠️ Technologies Used

* Python
* Python `datetime` module
* Python `time` module
* Python `platform` module
* Python `subprocess` module
* Python `os` module

## 📂 Project Structure

```text id="25xj6n"
Project Folder/
│
├── main.py
├── alarm.wav
└── README.md
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash id="z7mh1o"
git clone https://github.com/Harshit-Swain-25/Simple-Alarm-Clock.git
```

### 2. Navigate to the project folder

```bash id="ww9c4v"
cd Simple-Alarm-Clock
```

### 3. Run the program

```bash id="l6bf5j"
python main.py
```

No additional libraries are required.

## ⏰ Available Alarm Options

### Option 1: Set Alarm by Time

Set an alarm using the 24-hour format.

Example:

```text id="n4frrf"
14:30
14:30:15
```

### Option 2: Set Alarm by Countdown

Set an alarm after a specified number of seconds.

Example:

```text id="b9u07q"
10
30
60
```

## 🔔 Supported Notifications

The program supports different notification methods based on the operating system:

* macOS: `afplay`
* Windows: `winsound`
* Linux: `paplay` or `aplay`
* Fallback terminal beep support

## 🎯 Learning Objectives

This project helps beginners understand:

* Python functions
* User input validation
* Date and time manipulation
* Countdown timers
* Cross-platform programming
* File handling basics
* Command-line application development

## 👨‍💻 Author

Harshit Swain

GitHub: https://github.com/Harshit-Swain-25
