from dotenv import load_dotenv
import os 
import re 
import requests
import datetime
from github_contents import GithubContents
from bs4 import BeautifulSoup

load_dotenv()

gh_token = os.getenv('token')

endpoint = "/repos/{owner}/{repo}/forks"

url = 'https://api.github.com'
headers = {
    'Authorization' : f'token {gh_token}'
}

repo_info = {
    'owner': 'ironhack-datalabs',
    'repo': 'datamad1020'
}
parameters = {
    'state': 'all'
}

######## CHALLENGE 1 ########
print('\n')
print('--------------------------------- CHALLENGE 1 ---------------------------------')
print('\n')

data = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters)
data = data.json()

## 1 ##
forks = [fork['owner']['login'] for fork in data]

## 2 ##
name_lang = [(fork['full_name'], fork['languages_url']) for fork in data]

languages = {}
for link in name_lang:
    data = requests.get(link[1])
    soup = BeautifulSoup(data.text, 'html.parser')
    languages[link[0]] = soup.text

## 3 ##
print(languages)

######## CHALLENGE 2 ########
print('\n')
print('--------------------------------- CHALLENGE 2 ---------------------------------')
print('\n')

endpoint = "/repos/{owner}/{repo}/commits"
data = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters)
data = data.json()

## 1 ## 
lastw_commits = []
for commit in data:
    date = commit['commit']['committer']['date'].split('T')[0]
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    if date_obj >= datetime.datetime.strptime('2020-11-02', '%Y-%m-%d'):
        lastw_commits.append([commit['commit']['committer']['name'], 
                              commit['commit']['committer']['email'], 
                              datetime.datetime.strptime(commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')])

## 2 ##
print(len(lastw_commits))

######## CHALLENGE 3 ########
print('\n')
print('--------------------------------- CHALLENGE 3 ---------------------------------')
print('\n')    

url = 'https://api.github.com'
headers = {
    'Authorization' : f'token {gh_token}'
}
parameters = {
    'state': 'all'
}

data = requests.get(url+"/repos/ironhack-datalabs/scavenger/contents", headers=headers, params=parameters)
data = data.json()

paths_list = [element['path'] for element in data if element['path'] != '.gitignore']

scavengers = []
for path in paths_list:
    endpoint = f"/repos/ironhack-datalabs/scavenger/contents/{path}"

    data = requests.get(url+endpoint.format(path), headers=headers, params=parameters)
    data = data.json()

    for element in data:
        if '.scavengerhunt' in element['name']:
            scavengers.append((int(element['name'].replace('.', '').replace('scavengerhunt', '')), element['path']))

scavengers = sorted(scavengers)

github = GithubContents('ironhack-datalabs', 'scavenger', gh_token)

string = []
for file in scavengers:
    content, sha = github.read(file[1])
    string.append(content.decode('utf-8').strip())

string = ' '.join(string)
print(string)



