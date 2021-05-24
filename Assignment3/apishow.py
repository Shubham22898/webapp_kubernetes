import re
import json
import socket
import urllib.request as urllib3
import pytz
from datetime import datetime
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def get_info():
	url = 'http://ipinfo.io/json'
	response = urllib3.urlopen(url)
	data = json.load(response)
	result ={}

	result['IP']=data['ip']
	result['host']=socket.gethostname()
	
	result['city'] = data['city']
	result['region']=data['region']
	timezone = data['timezone']
	result['country']=data['country']
	
	IST = pytz.timezone(timezone)
	IST_time = datetime.now(IST)
	result['IST']=IST_time
	return render_template("fonts.html",result=result)

if __name__ == '__main__':
	app.run(debug=True)	
