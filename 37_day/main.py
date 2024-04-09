import requests
from datetime import datetime


pixela_endpoint = f'https://pixe.la/v1/users'
TOKEN = ...
USERNAME = ...
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
headers = {
    'X-USER-TOKEN': TOKEN
}
graph_params = {
    'id': 'graph1',
    'name': 'course_commits',
    'unit': 'commit',
    'type': 'int',
    'color': 'shibafu'
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

graph_post = f"{graph_endpoint}/{graph_params['id']}"
graph_post_config = {
    'date': datetime.today().strftime("%Y%m%d"),
    'quantity': '1'
}

# response = requests.post(url=graph_post, json=graph_post_config, headers=headers)
# print(response.text)