from github import Github
import os
from pprint import pprint
from github import InputGitAuthor

file_path = "requirements.txt"
g = Github("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")
repo = g.get_repo("stanlybolanos/FPMIR1T2022")


file = repo.get_contents(file_path, ref="main")  # Get file from branch
data = file.decoded_content.decode("utf-8")  # Get raw string data
data += "\npytest==5.3.2"  # Modify/Create file

def push(path, message, content, branch, update=False):
    author = InputGitAuthor(
        "Stanly",
        "stanly@stanly.com"
    )
    source = repo.get_branch("main")
    repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master
    if update:  # If file already exists, update it
        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
        repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
    else:  # If file doesn't exist, create it
        repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch

push(file_path, "Add pytest to dependencies.", data, "push2fork", update=True)