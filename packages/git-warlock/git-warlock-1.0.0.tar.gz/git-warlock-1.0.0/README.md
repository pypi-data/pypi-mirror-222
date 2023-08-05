# Git Warlock 🔮 - Git Remover Script

This Python script will remove all `.git` folders inside the directories of the current working directory.

## Currently working on

- Implementing user input path
- Creating a Python Package

## Description

The "Git Remover Script" is a command-line tool written in Python. It helps you remove all the `.git` folders found inside the visible directories of the current working directory. This script allows you to confirm your action before proceeding and provides visual feedback during the process.

## Features

- Confirmation prompt before starting the removal process.
- Visual indication of the confirmation prompt.
- Feedback on folders with deleted `.git` folders.

## Requirements

- Python 3.6 or higher
- Rich library (can be installed via `pip install rich`)

## How to Use

1. Place the script (`app.py`) in the directory where you want to remove the `.git` folders.
2. Open your terminal (command prompt) and navigate to the script's directory.
3. Run the script using the command:
   `python3 git-remove.py`
4. Follow the on-screen instructions to proceed or cancel the removal process.

## Important Note

This script can permanently delete `.git` folders, which will remove Git version control from those directories. Use it with caution and ensure you have a backup or are absolutely sure before proceeding.

## Author

The "Git Remover Script" is developed and maintained by [willywdev](https://github.com/willywdev).

## License

This project is licensed under the [MIT License](LICENSE).
