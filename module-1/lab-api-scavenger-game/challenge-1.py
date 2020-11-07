# enter your code below

# import requests

# data = requests.get("https://github.com/ironhack-datalabs/mad-oct-2018")

# forks  = data.json()
# fork.keys()

import requests
import os
from  dotenv import load_dotenv

data = requests.get("https://github.com/ironhack-datalabs/datamad1020")

load_dotenv ()
token = os.environ.get ( "api-token" )

