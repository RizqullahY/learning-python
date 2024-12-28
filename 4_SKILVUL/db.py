import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://raflyrizqullah:raflysabar@cluster0.jisamqd.mongodb.net/?retryWrites=true&w=majority")
db = client.SIC
my_collections = db.Mine

# def insert_data(kecepatan:90,latitude:6.2088,longitude:106.8456):
def insert_data(kecepatan,latitude,longitude):
    try:
        data = {
            "kecepatan" : kecepatan,
            "latitude" : latitude,
            "longitude" : longitude,
            "timestamp" : datetime.datetime.now()
        }
        hasil = my_collections.insert_one(data)
        print("Data telah terkirim dengan hasil",hasil)
        return True, None
    except Exception as e:
        return False,str(e)