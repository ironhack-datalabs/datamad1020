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
endpoint = "/repos/{owner}/{repo}/contents"
repo_info = {
    "owner":"ironhack-datalabs",
    "repo":"scavenger",
    "content":"content"
      
}

secretos = requests.get(url+endpoint.format(**repo_info),headers=headers,params = parameters).json()
print(secretos)

""""print("---------------------------------------------------------")
tree = secretos["tree"]

path = [tree[i]["path"] for i in range(len(tree))]
print(path)
lst = []
for d in path:
	if re.findall(r"hunt$",d):
		lst.append(d)
print("------------------------------------------------")

archivos = []
for e in lst:
	archivos.append(e[6:])
print(archivos)

https://api.github.com/ironhack-datalabs/scavenger/contents

#https://api.github.com/repos/ironhack-datalabs/scavenger/git/blobs

#path = [secretos[i]['path'] for i in range(len(secretos))]	
#print(path)
"""