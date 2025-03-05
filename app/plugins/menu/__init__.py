import logging
import os
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        """
        Lists all available commands in the 'commands' directory.
        """
        try:
            # Get current directory (commands/menu)
            commands_path = os.path.dirname(__file__)  
            # Go to the parent directory where other commands reside
            commands_dir = os.path.abspath(os.path.join(commands_path, ".."))  

            # List all command directories excluding __pycache__ and menu itself
            command_names = [
                d for d in os.listdir(commands_dir)
                if os.path.isdir(os.path.join(commands_dir, d)) and d not in ("__pycache__", "menu")
            ]

            if command_names:
                message = "Available commands: " + ", ".join(command_names)
            else:
                message = "No available commands found."

            logging.info(message)  # Log the available commands
            print(message)  # Print the output

        except FileNotFoundError:
            logging.error("Commands directory not found.")
            print("Error: Commands directory not found.")

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print(f"Error: {e}")
