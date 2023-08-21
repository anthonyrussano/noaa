from flask import Flask, render_template
import requests
import json
from vars import KEY

app = Flask(__name__)

API_KEY = KEY

def get_hurricane_data():
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:12&startdate=2021-08-01&enddate=2021-08-10&limit=1000"
    headers = {"token": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None

@app.route('/')
def index():
    data = get_hurricane_data()
    
    if data:
        return render_template('index.html', data=data)
    else:
        return "Could not get hurricane data"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
