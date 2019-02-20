import json
import datetime
import urllib.request

def getTime(event, context):
    current_time = datetime.datetime.now().time()
    body = "Hello, the current time is " + str(current_time)

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

def getWeather(event, context):

    raw = urllib.request.urlopen("https://api.darksky.net/forecast/58692974e7aa2bbd376d171346e9f89c/51.498038,-0.176455?units=si").read()
    contents = json.loads(raw)

    location = contents['timezone']
    weather = contents['currently']['summary']
    temp = contents['currently']['temperature']

    body = "In %s, the weather is %s, with a temperature of %dºC" % (location, weather, temp)

    response = {
        "statusCode": 200,
        "body": body
    }

    return response
