import requests
 
# requests
resp = requests.get('https://btu.edu.ge/')
print(type(resp))
print(resp)
#print(dir(resp))
print(resp.status_code)
# print(type(resp.status_code))
print(resp.headers)
print(resp.headers['Content-Type'])
print(type(resp.text))

# resp = requests.get('https://btu.edu.ge/wp-content/uploads/2021/07/logo_w-300x193.png')
# print(resp.content)
# file = open('test.png', 'wb')
# file.write(resp.content)
# file.close()


##https://openweathermap.org/ API
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
# resp = requests.get(url+'&mode=text')
# print(resp)
# print(resp.headers)
