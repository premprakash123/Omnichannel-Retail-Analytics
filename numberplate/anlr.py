import requests
from pprint import pprint
regions = ['in', 'it'] # Change to your country
with open('C:/Users/Innovation 4u/PycharmProjects/untitled6/Indian-Number-Plate-Recognition-System-master/Cars/0.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 0679d4a079f0e38ebf3b404cc43bfed101a9377e'})
result=response.json()
from pushover import init, Client

init("azvu6sc7bd25bfd2jcyw9tmeqmgqck")
Client("uo5ng47ujz7ff5fjo9jfxsrqzy8vo2").send_message("Hello!", title="Hello")
print(result)