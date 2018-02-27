#Get Wind information 
import json, requests

from datetime import datetime
now = datetime.now()

key = '95334bea145c2e1d0a8e824d42a4a345'
units = 'metric'
calgary_cityid = '5913490'
cityid = calgary_cityid
url = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)
weather = json.loads(url.text)


print(now)
print("%s" % now.hour, "%s" % now.minute, "%s" % now.second)

print weather['main']['temp'],"C"