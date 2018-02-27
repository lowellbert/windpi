#Get Wind information 
import datetime, time, json, requests
import RPi.GPIO as GPIO


#Servo Motor
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo_frequency = 50
servo_pwm = GPIO.PWM(servo_pin, servo_frequency)
servo_pwm.start(2.5)


def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servo_pin, True)
	servo_pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(servo_pin, False)
	servo_pwm.ChangeDutyCycle(0)

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


servo_pwm.ChangeDutyCycle(7.5)
time.sleep(3)
print "90 degrees"

servo_pwm.ChangeDutyCycle(2.5)
time.sleep(3)
print "0 degrees"

servo_pwm.ChangeDutyCycle(12.5)
time.sleep(3)
print "180 degrees"

servo_pwm.stop()
GPIO.cleanup()