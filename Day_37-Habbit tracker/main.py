import requests
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users"
TOKEN="fg5987gr4a5gaegjiaugjiL"
USERNAME="tanvi07"
GRAPH_ID="graph1"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

headers={
    "X-USER-TOKEN":TOKEN,
}

graph_config={
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"Hrs",
    "type":"float",
    "color":"sora"
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)

pixle_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"4.00",
}

# response=requests.post(url=pixle_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data={
    "quantity":"5.00",
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)