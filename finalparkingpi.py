from gpiozero import DistanceSensor
from gpiozero import LED
import  json
from time import sleep
from pubnub import Pubnub

lattitude = 13.040503
longitude =80.233692
distance = 0.2
sleepInterval = 5
locationName = 'VBC-Solitaire'

ds = DistanceSensor(echo=23,trigger=18,max_distance=0.2,threshold_distance=0.01)
led = LED(20)
print(ds.distance)

ds1 = DistanceSensor(echo=16,trigger=12,max_distance=0.2,threshold_distance=0.01)
led1 = LED(21)
print(ds1.distance)

ds2 = DistanceSensor(echo=27,trigger=17,max_distance=0.2,threshold_distance=0.01)
led2 = LED(19)
print(ds2.distance)

ds3 = DistanceSensor(echo=13,trigger=6,max_distance=0.2,threshold_distance=0.01)
led3 = LED(26)
print(ds3.distance)

publish_key = 'pub-c-b11b8c65-22c5-4bc7-84d2-dd41949dbc58'
subscribe_key='sub-c-313d4a34-2ef7-11e6-b700-0619f8945a4f'
pubnub = Pubnub(publish_key=publish_key,subscribe_key=subscribe_key)

def publishCallback(message):
	print(message)

while True:
	sleep(sleepInterval)	
	status = 'booked'  
	print("i-------------------")
	print(ds.distance)     
	print(ds1.distance)  
	print(ds2.distance)  
	print(ds3.distance)       
	if ds.distance  >= distance:
		status = 'available'
		led.on()
	else:
		led.off()
	publishMessage = {}
	publishMessage['name'] = locationName
	publishMessage['lattitude'] =  lattitude
	publishMessage['longitude'] = longitude
	publishMessage['slots'] = [{ 'name': 'l1','status':status}]
	message = json.dumps(publishMessage)
	pubnub.publish('parking_channel',  message, publishCallback, publishCallback)
	
	status = 'booked'	        
	if ds1.distance  >= distance:
		status = 'available'
		led1.on()
	else:
		led1.off()
	publishMessage1 = {}
	publishMessage1['name'] = locationName
	publishMessage1['lattitude'] =  lattitude
	publishMessage1['longitude'] = longitude
	publishMessage1['slots'] = [{ 'name': 'l2','status':status}]
	message = json.dumps(publishMessage1)
	pubnub.publish('parking_channel',  message, publishCallback, publishCallback)

	status = 'booked'	        
	if ds2.distance  >= distance:
		status = 'available'
		led2.on()
	else:
		led2.off()
	publishMessage2 = {}
	publishMessage2['name'] = locationName
	publishMessage2['lattitude'] =  lattitude
	publishMessage2['longitude'] = longitude
	publishMessage2['slots'] = [{ 'name': 'r1','status':status}]
	message = json.dumps(publishMessage2)
	pubnub.publish('parking_channel',  message, publishCallback, publishCallback)

	status = 'booked'	        
	if ds3.distance  >= distance:
		status = 'available'
		led3.on()
	else:
		led3.off()
	publishMessage3 = {}
	publishMessage3['name'] = locationName
	publishMessage3['lattitude'] =  lattitude
	publishMessage3['longitude'] = longitude
	publishMessage3['slots'] = [{ 'name': 'r2','status':status}]
	message = json.dumps(publishMessage3)
	pubnub.publish('parking_channel',  message, publishCallback, publishCallback)
