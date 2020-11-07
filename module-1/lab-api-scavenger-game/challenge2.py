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
    "state":"all",
    
    'until':'2020-11-01',
    'since':'2020-10-26'
   
    
    
}

url = "https://api.github.com"
endpoint = "/repos/{owner}/{repo}/commits"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"datamad1020"

    }

data = requests.get(url+endpoint.format(**repo_info), headers=headers, params=parameters).json()



print("-------------------------------------")




commits = [data[d]["commit"]["message"] for d in range(len(data))]
print(commits)
print(f"hay contenidos {len(commits)} commits de la semana pasada")


#https://api.github.com/repos/ironhack-datalabs/datamad1020/commits