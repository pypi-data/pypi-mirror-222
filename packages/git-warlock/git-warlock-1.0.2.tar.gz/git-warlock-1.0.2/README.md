# Git Warlock 🔮 - Git Remover Script

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This Python script will remove all `.git` folders inside the directories of the current working directory.

## Description 🔍

The "Git Remover Script" is a command-line tool written in Python. It helps you remove all the `.git` folders found inside the visible directories of the current working directory. This script allows you to confirm your action before proceeding and provides visual feedback during the process.

## Dependencies 🛠️

Git Warlock requires the following dependencies:

- `rich`

These dependencies will be automatically installed during the installation process using pip.

## Installation 🚀

You can install Git Warlock as a command-line executable using pip. Make sure you have Python 3.6 or above installed on your system.

```bash
pip3 install git-warlock
```

## How to Use 📚

After installing Git Warlock, you can run it as a command from any terminal. Simply type:

```
git-warlock
```

Git Warlock will then prompt you for confirmation to proceed with the removal of .git folders. Follow the on-screen instructions to continue or abort the process.

## Important Note ⚠️

This script can permanently delete `.git` folders, which will remove Git version control from those directories. Use it with caution and ensure you have a backup or are absolutely sure before proceeding.

## Author ✒️

Git Warlock was forged by willywdev 🔮. For more of my projects, visit my [GitHub profile](https://github.com/willywdev).

## License 📜

This project is licensed under the [MIT License](LICENSE).

## Build it yourself 🏗️

If you want to build Git Warlock from source or make modifications to the script, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/git-warlock.git
   ```

2. Navigate to the project directory:

   ```bash
   cd git-warlock
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

6. Now you can run the script:

   ```bash
   python git-warlock.py
   ```

Happy building and customizing your Git Warlock! If you have any questions or issues, feel free to open an [issue](https://github.com/your-username/git-warlock/issues) on the repository.
