# 🧞‍♀️ Voice Genie – Your Terminal-Based Voice Assistant

**Voice Genie** is a Python voice assistant built using Object-Oriented Programming (OOP) principles. It listens to your voice, understands your command, and performs real system-level actions — like opening Notepad, Google, or YouTube — right from your terminal.

This project uses modern tools like the `uv` package manager and the `subprocess` module to interact with your OS.

---

## 🎯 Features

- 🎙️ Voice recognition using your microphone
- 🗣️ Converts text to speech responses
- 🌦️ Real-time weather information using OpenWeatherMap API
- ⚙️ Opens Windows applications via `subprocess` (Notepad, Explorer, Calculator)
- 🌐 Opens websites like Google and YouTube
- 🤪 Tells jokes using the PyJokes library
- 💬 All built using Python OOP (organized classes and methods)
- ✅ Works fully in terminal – no GUI, no deployment needed

---

## 📁 File Structure

voice-genie/ ├── app.py # Main entry point ├── assistant.py # Voice assistant class ├── command_processor.py # All command logic ├── requirements.txt # uv-based dependency list └── .venv/ # Virtual environment (created by uv)



---

## 🛠️ Getting Started

### 1. Clone the project

```bash
git clone https://github.com/your-username/voice-genie.git
cd voice-genie
2. Set up environment with uv


bash
Copy code
uv venv
uv pip install -r requirements.txt
Or install packages manually:

bash
Copy code
uv pip install speechrecognition pyttsx3 pyaudio requests pyjokes openai

▶️ How to Run
Run the assistant from terminal:

bash
Copy code
uv venv
.venv\Scripts\activate
python app.py
Then speak only command :

"hello"

"open file explorer"

"what is your name"

"shutdown system"

"open google"

"open calculator"

"open youtube"

"What is the weather in Karachi?"

"Open notepad"

"Tell me a joke"

"What time is it?"

"Open Google"

"Exit"

🧠 How It Works
assistant.py: Listens to your voice and speaks responses

command_processor.py: Processes the command using if-elif logic

subprocess: Used to open apps like Notepad, Explorer, Calculator

requests: Fetches weather data from OpenWeatherMap

pyjokes: Tells fun jokes


🔑 Weather API Setup
Replace this line in command_processor.py with your real OpenWeatherMap API key:

python
Copy code
self.api_key = 'a049c7717fd938e05b88cdba663c3e17'
Get a free key at: https://openweathermap.org/api


💡Fututre Improvment:
Add OpenAI for AI-powered answers

Add reminders or task manager

Make it cross-platform (Linux/macOS)

Add GUI using Tkinter or PyQt



⚠️ Requirements
✅ Windows OS (because of subprocess and .exe commands)

✅ Python 3.10+

✅ Microphone and speaker

✅ Internet connection (for voice recognition + weather)


🙋‍♀️ Created By
Khadija Faisal
junior Developer & Designer
Class 07 Assignment – One Dollar OOP Challenge



