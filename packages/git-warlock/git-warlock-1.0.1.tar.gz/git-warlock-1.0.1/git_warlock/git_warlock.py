import os
import sys
import shutil
from rich import print as rprint

def main():
    # * Functions for Text Styling (rich)
    def make_text_yellow(text):
     return f"[bold yellow on black]{text}[/bold yellow on black]"

    def make_text_red_underlined(text):
        return f"[bold red underline]{text}[/bold red underline]"

    def make_text_bold(text):
        return f"[bold]{text}[/bold]"

    def make_text_cyan_on_dark_gray_background(text):
        return f"[bold cyan on dark_gray]{text}[/bold cyan on dark_gray]"

    def make_text_green_and_bold(text):
        return f"[bold green]{text}[/bold green]"

    def make_text_red_and_bold(text):
        return f"[bold red]{text}[/bold red]"

    # * Functions for Interactivity
    def get_user_confirmation(prompt):
        while True:
            rprint(make_text_yellow(prompt))
            user_input = input("(yes/no): ").strip().lower()
            if user_input in ["yes", "y"]:
                return True
            elif user_input in ["no", "n"]:
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no.'")

    # * Functions for Functionality
    def print_visible_folders():
        folders = [item for item in os.listdir(working_path) if os.path.isdir(os.path.join(working_path, item))]
        visible_folders = [folder for folder in folders if not folder.startswith(".")]
    
        if visible_folders:
            for folder in visible_folders:
                rprint("[bold green]" + folder + "[/bold green]")
        else:
            print("No visible folders found in the current directory.")

    def delete_git_folders():
        folders = [item for item in os.listdir(working_path) if os.path.isdir(os.path.join(working_path, item))]
        visible_folders = [folder for folder in folders if not folder.startswith(".")]

        deleted_folders = []
        for folder in visible_folders:
            git_folder_path = os.path.join(working_path, folder, ".git")
            if os.path.exists(git_folder_path) and os.path.isdir(git_folder_path):
                deleted_folders.append(git_folder_path)
                try:
                    shutil.rmtree(git_folder_path)  # Use shutil.rmtree() to remove non-empty directories.
                except OSError as e:
                    rprint(f"[bold red]Error:[/bold red] Could not delete .git folder in {folder} ({e})")
        return deleted_folders

    # * Program Start
    author_info = "Git Warlock: Forged by willywdev 🔮"
    github_profile = "GitHub: https://github.com/willywdev"
    print()
    rprint("[bold green]" + author_info + "[/bold green]")
    rprint("[bold green]" + github_profile + "[/bold green]")

    warning = "Read carefully!"
    message = "This Script will remove all .git Folders in All Folders in this directory."
    confirmation = "This cannot be restored. Are you sure about that?"
    working_path = os.getcwd()

    user_confirmation = "Do you want to proceed?\n"

    rprint()
    rprint(make_text_yellow(warning))
    rprint(make_text_bold(message))
    rprint(make_text_red_underlined(confirmation))
    rprint(make_text_cyan_on_dark_gray_background(working_path))
    confirmation = get_user_confirmation(user_confirmation)
    if confirmation:
        print("\nThese are all the folders in which .git is getting removed:\n")
    else: 
        print("\nBye.\n")
        sys.exit()

    print_visible_folders()
    proceed = get_user_confirmation("\nWould you like to proceed?\n")
    if proceed:
        print("coming soon")
        deleted_folders = delete_git_folders()
        if deleted_folders: 
            rprint(make_text_green_and_bold("\nThe following .git folders have been deleted:"))
            for folder in deleted_folders:
                print(folder)
        else:
            rprint(make_text_red_and_bold("\nNo .git folders were found."))
    else:
        print("\nBye.\n")
        sys.exit()

if __name__ == "__main__":
    main()