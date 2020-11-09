from dotenv import load_dotenv
import os
import requests

load_dotenv()

gh_token = os.getenv("GIT_TOKEN")
url = "https://api.github.com"
headers = {
    "Authorization": f"token {gh_token}"
}
endpoint = "/repos/{owner}/{repo}/forks"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"datamad1020"
} 
data = requests.get(url+endpoint.format(**repo_info), 
                    headers=headers).json()
new_url = data[5]['languages_url']
new_data = requests.get(new_url, headers=headers).json()


languages = []
for lang in new_data.keys():
    languages.append(lang)
print(languages)
