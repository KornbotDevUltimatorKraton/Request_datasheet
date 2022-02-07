import requests
while True:
   r = requests.get('http://192.168.1.37:8000/components')
   print(r.status_code)
   print(r.json())
