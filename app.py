from assistant import VoiceAssistant
from command_processor import CommandProcessor 

def main():
      assistant = VoiceAssistant()

      command_process = CommandProcessor(assistant)


      while True:
              # The assistant listens for a voice command
        command = assistant.listen()

        # If command is recognized, process it
        if command != "None":
            command_process.process_command(command)
        else:
                  print("No command recognized")

if __name__ == "__main__":
      main()
