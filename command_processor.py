import subprocess
import requests  # type: ignore
import pyjokes # type: ignore
import os

class CommandProcessor:
    def __init__(self, assistant):
        self.assistant = assistant
        self.api_key = 'a049c7717fd938e05b88cdba663c3e17' # weather api key

    def get_weather(self, city):
        """Fetch weather data for the given city"""
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            
            if data["cod"] != 200:
                return "Sorry, I couldn't fetch the weather data."

            main = data["main"]
            weather_description = data["weather"][0]["description"]
            temperature = main["temp"]
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        except Exception as e:
            return "Sorry, there was an error fetching the weather."
        
    def notepad(self):
        """Open notepad"""
        subprocess.Popen(["notepad.exe"])
  
    def calculator(self):
        """Open calculator"""
        subprocess.Popen(["calc.exe"])

    def open_file(self):
        """Open a file explorer"""
        subprocess.Popen("C:\\Windows\\explorer.exe")
        
    def shutdown_system(self):
        """Shutdown the system"""
        os.system("shutdown /s /f /t 1")
    
    def process_command(self, command):
        """Process the voice command"""
        if "hello" in command:
            self.assistant.speak("Hello, how can I help you today?")
        elif "what is your name" in command:
            self.assistant.speak("I am a voice assistant created by you my name is jarvis.")

        elif "what is the weather in" in command:
            city = command.split("in")[-1].strip()  # Extract the city name from the command
            weather_info = self.get_weather(city)
            self.assistant.speak(weather_info)
    
        elif "what time is it" in command:
            from datetime import datetime
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            self.assistant.speak(f"The current time is {time}.")
        elif "shutdown system" in command:
            self.shutdown_system()
            self.assistant.speak("System will shutdown in 1 second.")
        elif "open file explorer" in command:
            self.open_file()
            self.assistant.speak("Opening file explorer.")

        elif "open google" in command:
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://www.google.com"])
            self.assistant.speak("Opening Google.")

        elif "open youtube" in command:
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "https://youtube.com"])
            self.assistant.speak("Opening YouTube.")

        elif "open notepad" in command:
            self.notepad()
            self.assistant.speak("Opening Notepad.")

        elif "open calculator" in command:
            self.calculator()


        elif "tell me a joke" in command:
            joke = pyjokes.get_joke()
            self.assistant.speak(joke)

        elif "exit" in command:
            self.assistant.speak("Goodbye thanks for using me!")
            exit()        
        else:
            self.assistant.speak("Sorry, I didn't understand that.")
