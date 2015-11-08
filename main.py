"""Cloud Foundry Implementation"""
from flask import Flask, request
import os
import mente
from sqlalchemy import desc
from models import Beacon, Location
from decorators import crossdomain

app = Flask(__name__, static_folder='DementiaHackWebsite', static_url_path='')

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/', methods=['GET', 'POST'])
@crossdomain(origin='*')
def hello_world(): 	
	return 'Hello World';
    # read and return a static web page, because why not

@app.route('/datapush/', methods=['POST'])
def datapush():
	# this needs to process incoming data and store that data in the database

	#data push, 3 names 3 values
    
    #Convert all signal strengths to distances
    #y = -9.048ln(x) - 68.101 , y is signal strength in dB, x is distance from beacon in m
    # solving for:  x =  e ^((y + 68.101)/(-9.048))
    
    
    #Convert to circles, cenered at 0,0 for Bean 1
    #0,5 for bean 2
    #5,0 for bean 3
    
    
    #find intersections of circles 1 and 2
    
    
    #see which one is closest to intersecting with circle 3/within circle 3
    
    
	return 'Pushed';

	
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
