import requests
import json
from time import sleep
from twilio.rest import Client

#twillio junk
account = "ACa67e6af394384a65f7c7a0c4480df5b5"
token = "03e12ff0f30e9ff6d603bdd8c36ec798"
client = Client(account, token)
message = client.messages.create(to="+15173958962", from_="+12568040990", body="Your toast is done!")

#file_name = os.getcwd()+'/test.png'


#this is the heroku sign-in, it will get a session opened with a cookie
url = 'http://secure-garden-32931.herokuapp.com/users/sign_in'
payload ={'user': {'email': 'petershutt00@gmail.com', 'password':'hackerfellows'}}
headers = {'content-type': 'application/json'}
 
r = requests.post(url, data=json.dumps(payload), headers=headers)


#url2 = 'https://secure-garden-32931.herokuapp.com/posts'
#payload2 = {'authenticity_token':'FD3BqJRnTbXjjCaneULwd1y1H+7cM1KYpghz+8eV4gyPzTfuOoMfMauN+TVrIeok80vbTfVt9+JUYmlJ097M9g==','post': {'attachment':fh,'content': 'test from python'}}

#r2 = requests.post(url2, data=json.dumps(payload2),cookies=r.cookies, headers=headers)
#print(r2.content)


