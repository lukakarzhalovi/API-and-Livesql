import requests
import json


# ##https://openweathermap.org/ API
# lat = 41.785978
# long = 44.743510
# API_key = 'e84f7eb383b5f0bf9172c08cd14c984b'
# url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_key}'
# resp = requests.get(url + '&units=metric')
# print(resp)
# print(resp.text)

# city_name = 'Tbilisi'
# API_key = 'e84f7eb383b5f0bf9172c08cd14c984b'
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
# resp = requests.get(url+'&mode=xml')
# print(resp)
# print(resp.text)



# city_name = 'Tbilisi' 
# #city_name = input('city name: ')
# API_key = 'e84f7eb383b5f0bf9172c08cd14c984b'

# payload = {'q':city_name, 'appid':API_key, 'units':'metric'}
# url = f'https://api.openweathermap.org/data/2.5/weather'

# resp = requests.get(url, params=payload)

# print(resp.url)
# print(resp)
# print(resp.text)
# print(resp.json()['weather'])
# print(type(resp.json()))
# j = json.loads(resp.text)
# print(j)
# print(json.dumps(j, indent=4))
# print(j['main']['temp'])  

## status code 404

# res = json.loads(resp.text)
# with open('data.json', 'w') as f:
#     json.dump(res, f, indent=4)


## NASA
# api_key = 'PHtbTdNUe4kbB43QihYfS4LRdeQTwxslA5hUIyoi'
# payload = {'api_key':api_key}
# url = 'https://api.nasa.gov/planetary/apod'
# r = requests.get(url, params=payload)
# res = r.json()
# #print(r.json())
# print(json.dumps(res, indent=4))

# img_url = res['hdurl']
# img_resp = requests.get(img_url)
# print(img_resp)

# with open('nasa.jpg','wb') as f:
#     f.write(img_resp.content)