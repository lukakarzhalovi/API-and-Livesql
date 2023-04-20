import requests
import json
import sqlite3

lat = 41.793045
lon = 44.763806
api_key = "e84f7eb383b5f0bf9172c08cd14c984b"
resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
print(resp)
#print(type(resp.json()))
j = json.loads(resp.text)
data = json.dumps(j,indent=4)
print(j["main"])
if resp.status_code >= 200 and resp.status_code <= 300:
    conn = sqlite3.connect("weathet.sqlite")
    cursor = conn.cursor()
    # cursor.execute('''CREATE TABLE weather(
    #             key VARCHAR(25),
    #             value FLOAT (25)
    # ) ''')
    for key,value in j["main"].items():
        cursor.execute('''INSERT INTO weather(key,value) VALUES("{}","{}")'''.format(key,value))
        conn.commit()
        conn.close()
        print(key,value)
else:
    print("ვებგვერდზე წვდომა შეუძლებელია")



