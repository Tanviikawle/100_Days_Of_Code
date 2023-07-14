import requests

OWM_Endpoint="https://api.openweathermap.org/data/2.5/weather"
api_key="09fa0d197a65991460a49c7520d01d1e"
parameters={
    "lat":19.075983,
    "lon":72.877655,
    "API key":api_key
}


response=requests.get(url=OWM_Endpoint,params=parameters)
response.raise_for_status()
print(data=response.json())


