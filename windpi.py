#Get Wind information 
import json, requests

key = '95334bea145c2e1d0a8e824d42a4a345'
units = 'metric'
calgary_cityid = '5913490'
cityid = calgary_cityid
url = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)
value = datetime.datetime.fromtimestamp(weather['dt'])

weather = json.loads(url.text)

print weather['name'], weather['sys']['country']
print weather['dt']
print weather['main']['temp'],"C"
print weather['wind']['speed'], "meter/sec"
print weather['wind']['deg'], "degrees"
