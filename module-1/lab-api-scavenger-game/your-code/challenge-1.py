from dotenv import load_dotenv
import os 
import re 
import requests
import datetime

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

data = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters)

data = data.json()

## 1 ##

#forks = [fork['owner']['login'] for fork in data]

## 2 ##

#languages = [fork['languages_url'] for fork in data]  #### APILAR LOS ENLACES

## 3 ##

#print(languages)

######## CHALLENGE 2 ########

#endpoint = "/repos/{owner}/{repo}/commits"
#data = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters)
#data = data.json()

## 1 ## 

#lastw_commits = []
#for commit in data:
 #   date = commit['commit']['committer']['date'].split('T')[0]
 #   date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
 #   if date_obj >= datetime.datetime.strptime('2020-11-02', '%Y-%m-%d'):
  #      lastw_commits.append([commit['commit']['committer']['name'], 
   #                           commit['commit']['committer']['email'], 
   #                           datetime.datetime.strptime(commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')])

## 2 ##

#print(len(lastw_commits))

######## CHALLENGE 3 ########
    



