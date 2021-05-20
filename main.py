import requests
import os
from datetime import datetime

USERNAME = "guidedryan"
GRAPH = "a1"

pizela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": os.environ["pixela_key"],
    "username": "guidedryan",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# The call to create the account

#response = requests.post(url=pizela_endpoint, json=user_params)


# Creating the graph:
graph_endpoint = f"{pizela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "a1",
    "name": "Coding graph",
    "unit": "Projects worked on",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": os.environ["pixela_key"]
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


today = datetime.now()


#Posting pixel to the graph

add_val_endpoint = f"{graph_endpoint}/{GRAPH}"

add_val_config = {
    #"date": today.strftime("%Y%m%d"),
    "date": "20210516",
    "quantity": "29",
}

#response = requests.post(url=add_val_endpoint, json=add_val_config, headers=headers)
# Check the response text for more information on passing
#print(response.text)

change_val_endpoint = f"{add_val_endpoint}/20210516"

change_val_config = {
    "quantity": "1"
}

#Update
#response = requests.put(url=change_val_endpoint, json=change_val_config, headers=headers)


#Delete
#response = requests.delete(url=change_val_endpoint, headers=headers)
