"""Cloud Foundry Implementation"""
from flask import Flask, request
import os
import mente
from sqlalchemy import desc
from models import Beacon, Location
import math
import datetime

from decorators import crossdomain

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/', methods=['GET', 'POST'])
@crossdomain(origin='*')
def hello_world():
	return 'Hello World';
    # read and return a static web page, because why not

@app.route('/datapush/', methods=['POST'])
def datapush(strength_1, strength_2, strength_3):
	# this needs to process incoming data and store that data in the database
	#data push, 3 names 3 values
    
    #Convert all signal strengths to distances
    #y = -9.048ln(x) - 68.101 , y is signal strength in dB, x is distance from beacon in m
    # solving for:  x =  e ^((y + 68.101)/(-9.048))
    r1=math.exp((strength_1+68.101)/-9.048);
    r2=math.exp((strength_2+68.101)/-9.048);
    r3=math.exp((strength_3+68.101)/-9.048);
    
    center1=[0,0]
    center2=[0,5]
    center3=[5,0]
    
    poi=[];
    #Convert to circles, centered at 0,0 for Bean 1
    #0,5 for bean 2
    #5,0 for bean 3
    
    #find intersections of 2 of the circles (try 1 & 2, 1 & 3, 2 & 3)
    #If circles 1 and 2 intersect
    d_1_2=r1+r2
    d_1_3=r1+r3
    d_2_3=r2+r3
    

    if 5 <= d_1_2:
        poi=findIntersect(r1, r2, r3, center1, center2, center3)
    elif 5 <= d_1_3:
        poi=findIntersect(r1, r3, r2, center3, center2, center1)
    elif 5 <=d_1_3:
        poi=findIntersect(r2, r3, r1, center2, center3, center1)
    else:
        return
    
    loc=Location('0x0000', poi[1], poi[2], datetime.Now())
    mente.get_session().add(loc)
    mente.getsession().commit()
    
    return 'Pushed';

    #find intersections of circles 1 and 2
    
    
    #see which one is closest to intersecting with circle 3/within circle 3


#A and B are 2 circles touching, C is third circle
def findIntersect(rA, rB, rC, centerA, centerB, centerC):
        a=(math.pow(rA,2)-math.pow(rB,2)+math.pow(rA+rB))/(2*(rA+rB))
        #a=r1 when circles touch at a point
        h=math.sqrt(math.pow(rA,2)-math.pow(a,2))   
        pIntersect_1=centerA+[a,h]
        pIntersect_2=centerA+[a,-h]
        
        #find which point is closer to circumference of third circle
        d_to_pIntersect_1=math.fabs(math.sqrt((pIntersect_1[1]-centerC[1])**2-(pIntersect_1[2]-centerC[2])**2)-r3)
        d_to_pIntersect_2=math.fabs(math.sqrt((pIntersect_2[1]-centerC[1])**2-(pIntersect_2[2]-centerC[2])**2)-r3)
        
        if d_to_pIntersect_1 >= d_to_pIntersect_2:
            poi=pIntersect_2
        else:
            poi=pIntersect_1
        
        return poi
	
@app.route('/datapull/', methods=['POST'])
@crossdomain(origin='*')
def datapull():
	# this needs to provide the most recent data from the database
	import json
	uuid = request.form.get('uuid')
	if uuid is None:
		return '{}';
	
	result = Location.query.filter(Location.uuid==uuid).order_by(desc(Location.time)).first()
	if result:
		return result.to_json();
	else:
		return '{}'

@app.route('/datatest/', methods=['GET'])
def datatest():
	beacons = Beacon.query.all()
	text = '<html><body><p>'
	for beacon in beacons:
		text = text + beacon.uuid + ' at (' + str(beacon.x) +', '+ str(beacon.y) + ')<br />'
	text = text + '</p></body></html>'
	return text
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
	
	
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
