import requests
from datetime import datetime


APP_ID = '87f68c70'
API_KEY = '9651e7cf4c2742ba4ebccf7c7546ddce'
SHEETY_URL = 'https://api.sheety.co/484c65498cd171cecedc4323533acb71/myWorkouts/workouts'

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}


user_query = input('Tell me what exercises have you done?: ')
app_query = {
    'query': user_query,
}


response = requests.post(url=url, headers=headers, json=app_query)
exercises_data: dict = response.json()['exercises']

for exercise in exercises_data:
    exercise_dict = {
        'workout': {
            'date': datetime.today().strftime("%d/%m/%Y"),
            'time': datetime.now().strftime("%H:%M:%S"),
            'exercise': exercise['name'].title(),
            'duration': str(exercise['duration_min']),
            'calories': exercise['nf_calories']
        }
    }
    sheet_response = requests.post(url=SHEETY_URL, json=exercise_dict)
    print(sheet_response.text)
