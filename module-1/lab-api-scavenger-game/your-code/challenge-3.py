from dotenv import load_dotenv
import os
import re
import requests

load_dotenv()

gh_token = os.getenv("GIT_TOKEN")
url = "https://api.github.com"
headers = {
    "Authorization": f"token {gh_token}"
}
endpoint = "/repos/{owner}/{repo}/contents"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"scavenger"
} 
data = requests.get(url+endpoint.format(**repo_info), 
                    headers=headers).json()
file_links = {}

for word in data[1:]:

    new_url = word['url']
    new_data = requests.get(new_url, headers=headers).json()

    for word in new_data:

        if re.search('scavengerhunt$', word['name']) is not None:
            scavenger_name = word['name']
            scavenger_url = word['git_url']
            file_links[scavenger_name] = scavenger_url
sorted_file_links = dict(sorted(file_links.items()))
values = sorted_file_links.values()
for val in values:
    print(val)