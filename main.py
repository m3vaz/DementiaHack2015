"""Cloud Foundry Implementation"""
from flask import Flask
import os

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/')
def hello_world():
	f = open('sharks.html')
	return f.read();
    # read and return a static web page, because why not

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
