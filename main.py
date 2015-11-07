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
    #y = -9.048ln(x) - 68.101 , y is signal strength in dB, x is distance from beacon in m
    # solving for:  x =  e ^((y + 68.101)/(-9.048))
    
    
    
	return 'Pushed';
	
@app.route('/datapull/', methods=['GET'])
def datapull():
	# this needs to provide the most recent data from the database
	return 'Pulled';
	

	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
