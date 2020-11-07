from dotenv import load_dotenv
import requests
import os
import re
import pandas as pd

load_dotenv()
gh_token = os.getenv("TOKEN")

headers = {
    "Authorization": f"token {gh_token}"
}
parameters = {
    "state":"all"
}

url = "https://api.github.com"
endpoint = "/repos/{owner}/{repo}/forks"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"datamad1020"
}


data = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters).json()

print("---------------------------------------------------------")
#data = requests.get('https://api.github.com/repos/ironhack-datalabs/datamad1020/forks').json()
#print(data)


forks = [data[i]["owner"]["login"] for i in range(len(data))]
print(forks)
print("-----------------------------------------")
language = [data[i]["language"] for i in range(len(data))]

lenguages = []
for l in language:
	if l != None and l not in lenguages:
		lenguages.append(l)
print(lenguages)
print("-------------------------------------------------------")
"""
endpoint = "/repos/{owner}/{repo}/search/commits"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"datamad1020"
}
url_commits = requests.get(-H "Accept: application/vnd.github.cloak-preview+json"'https://api.github.com/search/commits?q=repo:ironhack-datalabs/datamad1020',headers=headers, params = parameters).json()
print(url_commits)


#commits = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters).json()
"""