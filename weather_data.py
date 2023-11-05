import requests, json

API_key=open('api_key','r') #My API key

url="http://api.openweathermap.org/data/2.5/weather?"

name=input("Enter city name:")

full_url=url+"appid="+API_key+"&q="+name

res=requests.get(full_url)

a=res.json()
if a["cod"]!=404:
    b=a["main"]
    temperature=b["temp"]
    pressure=b["pressure"]
    hum=b["humidity"]
    c=a["weather"]
    desc=c[0]["description"]
    print("Temperature ="+str(temperature)+
          "\n Atmospheric Pressure ="+str(pressure)+
          "\n Humidity ="+str(hum)+
          "\n Description ="+str(desc) )
else:
    print("city not found")

    
