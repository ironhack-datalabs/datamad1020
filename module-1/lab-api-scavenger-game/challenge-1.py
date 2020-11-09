import requests
import os
data = requests.get("https://github.com/ironhack-datalabs/datamad1020")


from  dotenv import load_dotenv
load_dotenv ()
token = os.environ.get ( "api-token" )

