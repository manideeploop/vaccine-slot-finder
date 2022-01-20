import requests
import json 


pin=input('Enter the Pincode: ')
date=input('Enter the date in (DD-MM-YYYY) Format: ')

URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pin,date)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for x in data:
        counter += 1
        print(x['name'],x['fee_type'],x['from'],x['to'],x['address'])
        
    if(counter == 0):
        print("No slots available.....!")
        
        

findAvailability()
