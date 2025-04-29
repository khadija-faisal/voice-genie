import speech_recognition as sr  # type: ignore
import pyttsx3  # type: ignore


class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()


    def speak(self, texts):
        """Method to convert text to speech"""
        self.engine.say(texts)
        self.engine.runAndWait()

    def listen(self):
        """Method to listen for voice input"""
        with sr.Microphone() as source: # Use the microphone to listen
            print("Listening...")
            audio = self.recognizer.listen(source)
            
        try: 
            command = self.recognizer.recognize_google(audio)
            print(f"Recognized command: {command}") 
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return "None"
        except Exception as e:
            print("Error: ", e)
            return "None"
        


