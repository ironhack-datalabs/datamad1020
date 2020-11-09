import requests
import json
import os
from dotenv import load_dotenv

## CHALLENGE 1
load_dotenv()
git_token = os.getenv("GIT_TOKEN")

# GET /repos/:owner/:repo/forks
url = "https://api.github.com/"
endpoint = "repos/{owner}/{repo}/forks"
repo_info = {"owner":"ironhack-datalabs",
        "repo":"madrid-oct-2018"}

headers = {'Authorization': f'token {git_token}'}

git_data = requests.get(url + endpoint.format(**repo_info), headers=headers)

git_data = git_data.json()
languages = set([dic['language'] for dic in git_data if dic['language'] != None])
print(languages)

## CHALLENGE 2
commits_url = set([com['commits_url'] for com in git_data if com['commits_url'] != None])
commit_data = [requests.get(link[:-6]).json() for link in commits_url]
messages = [
    commit['commit']['message']
    for user in commit_data
        for commit in user
            if commit['commit']['message'] != None and commit['commit']['message'] != ''
]
print(len(messages))

## Challenge 3
endpoint = "repos/{owner}/{repo}/contents"
repo_info = {"owner":"ironhack-datalabs",
        "repo":"scavenger"}
scavenger = requests.get(url + endpoint.format(**repo_info), headers=headers)
scavenger = scavenger.json()
file_content = [requests.get(file['url'], headers=headers).json() for file in scavenger if file['name'] != '.gitignore']
result = [
    requests.get(hunt['url'], headers=headers).json()
    for file in file_content
        for hunt in file
            if '.scavengerhunt' in hunt['name']
]