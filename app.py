## test.py
import serial
from flask import Flask
from flask_ask import Ask, statement, question, session
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
