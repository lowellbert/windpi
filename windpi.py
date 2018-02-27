#Get Wind information 
import datetime, json, requests
import RPi.GPIO as GPIO
from time import sleep

#Servo Motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(18, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(18, False)
	pwm.ChangeDutyCycle(0)

#City Ids
calgary_cityid = '5913490'

#OpenWeatherMap information
key = '95334bea145c2e1d0a8e824d42a4a345'
units = 'metric'
cityid = calgary_cityid
url = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)
weather = json.loads(url.text)
value = datetime.datetime.fromtimestamp(weather['dt'])
wind_degrees = weather['wind']['deg']

print weather['name'], weather['sys']['country']
print weather['dt']
print(value.strftime('%Y-%m-%d %H:%M:%S'))
print weather['main']['temp'],"C"
print weather['wind']['speed'], "meter/sec"
print weather['wind']['deg'], "degrees"

SetAngle(0)
sleep(2)
SetAngle(wind_degrees)

pwm.stop()
GPIO.cleanup()