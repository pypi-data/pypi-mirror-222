
import os
import shutil

# function that will later be used to execute a given list of commands (when there are numerous commands, not for single prompts)
def execute_commands(commands_to_execute):
    for cmd in commands_to_execute:
        os.system(cmd) # the os module provides an easy way to execute prompt commands

# function to download a repository in a given path of your computer
def download_repo(github_repository_url, folder_path="local"):
    if folder_path == "local":
        folder_path = os.path.abspath(os.path.dirname(__file__))

    # in case where github's project page url given with .git we'll remove it to avoid conflicts
    if ".git" in github_repository_url:
        github_repository_url = github_repository_url.replace(".git", "")

    os.chdir(folder_path)
    os.system(f"git clone {github_repository_url}")

# function to initiate a repository (when uploading for the first time)
def init_repo(github_repository_url, add_readme="noreadme", folder_path="local"):
    # to initiate GitHub repo in current directory, default parameter is set to local for this purpose
    if folder_path == "local":
        folder_path = os.path.abspath(os.path.dirname(__file__))

    # in case where github's project page url given with .git we'll remove it to avoid conflicts
    if ".git" in github_repository_url:
        github_repository_url = github_repository_url.replace(".git", "")

    commands_to_execute = ["git init",
                           f"git remote add origin {github_repository_url}.git"]

    #adding README to commands if desired
    if add_readme == "readme":
        commands_to_execute.append("add README.md")

    elif add_readme == "noreadme":
        pass # In case where you don't want to have a readme in your files

    os.chdir(folder_path)
    execute_commands(commands_to_execute)

def commit_files(branch_name, commit_message, folder_path="local"):
    # "local" means nothing, need to replace by actual local path
    if folder_path == "local":
        folder_path = os.path.abspath(os.path.dirname(__file__))

    commands_to_execute = ["git add --all",
                           f"git commit -m '{commit_message}'",
                           f"git branch -M {branch_name}",
                           f"git push -u origin {branch_name}"
                           ]

    os.chdir(folder_path)
    execute_commands(commands_to_execute) #executing required commands to commit files

def create_file(file_name, file_extension="txt", file_content="", file_path="local"):
    if file_path == "local":
        file_path = os.path.abspath(os.path.dirname(__file__))

    # Generate the full file path with extension
    new_file_path = os.path.join(file_path, f"{file_name}.{file_extension}")

    if file_content == "":
        # Create an empty file using shutil
        shutil.copy(os.devnull, new_file_path)

    else:
        # Write the file content to the new file
        with open(new_file_path, 'w') as file:
            file.write(file_content)
