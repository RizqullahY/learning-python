import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   api_url = 'https://example.com/api/data'  # Ganti dengan URL API yang sesuai
   response = requests.get(api_url)
   
   if response.status_code == 200:
      data = response.json()
      water_level = data['water_level']
      temperature = data['temperature']
   else:
      water_level = '-'
      temperature = '-'
   
   return render_template('index.html', water_level=water_level, temperature=temperature)

if __name__ == '__main__':
   app.run()
