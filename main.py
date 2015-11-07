"""Cloud Foundry Implementation"""
from flask import Flask
import os

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	return 'Hello World';
    # read and return a static web page, because why not

@app.route('/datapush/', methods=['POST'])
def datapush():
	# this needs to process incoming data and store that data in the database
	#data push, 3 names 3 values
    
    #Convert all signal strengths to distances
    
    
    #Convert to circles, cenered at 0,0 for Bean 1
    #0,5 for bean 2
    #5,0 for bean 3
    
    
    #find intersections of circles 1 and 2
    
    
    #see which one is closest to intersecting with circle 3/within circle 3
    
    return 'Pushed';
	
@app.route('/datapull/', methods=['GET'])
def datapull():
	# this needs to provide the most recent data from the database
	return 'Pulled';
	

	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
