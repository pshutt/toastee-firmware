## test.py
import serial
from flask import Flask
from flask_ask import Ask, statement, question, session
import requests
import json
import os
from time import sleep
from twilio.rest import Client

#twillio junk
account = "ACa67e6af394384a65f7c7a0c4480df5b5"
token = "03e12ff0f30e9ff6d603bdd8c36ec798"
client = Client(account, token)
#message = client.messages.create(to="+15173958962", from_="+12568040990", body="Your toast is done!")

app = Flask(__name__)
ask = Ask(app, '/')
ser = serial.Serial('/dev/ttyACM0')

@ask.launch
def start_skill():
    try:
        ser = serial.Serial('/dev/ttyACM0')
    except:
        pass
    welcome_message = 'Get ready for some GREAT toast! Would you like your toast; light, medium or dark?'
    return question(welcome_message)



#these are the settings for light, medium and dark toast.
@ask.intent('start_light_toast')
def start_toast():
    ser = serial.Serial('/dev/ttyACM0')
    ser.write('2')
    sleep(120)
    post()
    return statement('Making light toast!')


@ask.intent('start_medium_toast')
def start_toast():
    ser = serial.Serial('/dev/ttyACM0')
    ser.write('4')
    return statement('Making medium toast!')

@ask.intent('start_dark_toast')
def start_toast():
    ser = serial.Serial('/dev/ttyACM0')
    ser.write('6')
    return statement('Making dark toast!')



#this will stop the toaster

@ask.intent('stop_toast')
def stop_toast():
    ser = serial.Serial('/dev/ttyACM0')
    ser.write('0')
    return statement('stopping toaster!')

@ask.session_ended
def session_ended():
    try:
       # ser.write('1')
        ser.close()
    except:
        pass
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True)


def post():
    message = client.messages.create(to="+15173958962", from_="+12568040990", body="Your toast is done!")
    file_name = os.getcwd()+'/image.jpg'
    blob = json.dumps(file_name.encode("base64"))
    #this is the heroku sign-in, it will get a session opened with a cookie
    url = 'http://secure-garden-32931.herokuapp.com/users/sign_in'
    payload ={'user': {'email': 'petershutt00@gmail.com', 'password':'hackerfellows'}}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    url2 = 'https://secure-garden-32931.herokuapp.com/posts'
    payload2 = {'authenticity_token':'FD3BqJRnTbXjjCaneULwd1y1H+7cM1KYpghz+8eV4gyPzTfuOoMfMauN+TVrIeok80vbTfVt9+JUYmlJ097M9g==','post': \
    {'content': 'test from python new  ' + blob + ' 37.JPG'}}

    r2 = requests.post(url2, data=json.dumps(payload2),cookies=r.cookies, headers=headers)
