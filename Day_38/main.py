import requests
from datetime import datetime


APP_ID="91ef72fb"
API_KEY="3fb6c094cec577938aa744cb1a9af775"
GENDER = "female"
WEIGHT_KG = 43
HEIGHT_CM = 167.64
AGE = 20

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/a629cd10de7913652a133102a77ac0d1/workoutTracking/workouts"

exercise=input("Tell me which exercise you did : ")

headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "Content-Type": "application/json",
    "Authorization": "Basic VGFudmk6MTIzNDU2",
}

api_data={
    "query":exercise,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

response=requests.post(url=endpoint,json=api_data,headers=headers)
result=response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            "Tanvi", 
            "123456",
        )
        )    
    print(sheet_response)

    

