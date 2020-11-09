from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()

gh_token = os.getenv("GIT_TOKEN")
url = "https://api.github.com"
headers = {
    "Authorization": f"token {gh_token}"
}
endpoint = "/repos/{owner}/{repo}/commits"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"datamad1020"
} 
data = requests.get(url+endpoint.format(**repo_info), 
                    headers=headers).json()


this_weeks_commits = []
for item in data:
    date = item['commit']['author']['date'].split('T')
    if date[0] in pd.date_range(start='2020-11-01', end='2020-11-07'):
        this_weeks_commits.append(date[0]) 
print(f"There have been {len(this_weeks_commits)} commits made this week.")       