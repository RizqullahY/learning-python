from flask import Flask , request
from db import insert_data

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World!'

@app.route('/test',methods=['GET','POST'])
def pesan():
    if request.method == 'GET':
        return "ini method get"
    elif request.method == 'POST':
        return "ini method post"

@app.route('/data',methods=['GET','POST'])
def data_2():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    insert_data(kecepatan=kecepatan, latitude=latitude, longitude=longitude)

    return{"message":"data telah terkirim"
        
    }


if __name__ == '__main__':
    app.run(debug=True)


