from app.commands import Command
import os

class MenuCommand(Command):
    def execute(self):
        """
        Lists all available commands in the 'commands' directory.
        """
        commands_path = os.path.dirname(__file__)  # Get current directory (commands/menu)
        commands_dir = os.path.abspath(os.path.join(commands_path, ".."))  # Go to 'commands' directory

        # List all command directories excluding __pycache__ and menu itself
        command_names = [
            d for d in os.listdir(commands_dir)
            if os.path.isdir(os.path.join(commands_dir, d)) and d not in ("__pycache__", "menu")
        ]

        print("Available commands:", ", ".join(command_names))


