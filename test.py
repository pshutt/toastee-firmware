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
    welcome_message = 'Are you ready for some GREAT toast?'
    return question(welcome_message)


@ask.intent('start_toast')
def start_toast():
    ser = serial.Serial('/dev/ttyACM0')
    ser.write('0')
    return statement('making toast!')

@ask.intent('stop_toast')
def stop_toast():
    ser = serial.Serial('/dev/ttyACM0')
    ser.write('1')
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
