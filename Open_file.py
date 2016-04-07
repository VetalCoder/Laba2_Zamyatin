import pickle
import json
import yaml
from dateutil import parser
import datetime


def convert_to_json_format(obj):
    tmp = {}
    for i in obj:
        tdate = str(i)
        ttemp = obj[i][0]
        tpreasure = obj[i][1]
        thumidity = obj[i][2]
        twspeed = obj[i][3]
        twdirect = obj[i][4]
        tprec = obj[i][5]
        ttmp = {tdate: [ttemp, tpreasure, thumidity, twspeed, twdirect, tprec]}
        tmp.update(ttmp)
    return tmp


def convert_to_normal_format(obj):
    tmp = {}
    for i in obj:
        tdate = parser.parse(i)
        tdate_trunc = datetime.date(tdate.year, tdate.month, tdate.day)
        ttemp = int(obj[i][0])
        tpreasure = int(obj[i][1])
        thumidity = int(obj[i][2])
        twspeed = float(obj[i][3])
        twdirect = obj[i][4]
        tprec = obj[i][5]
        ttmp = {tdate_trunc: [ttemp, tpreasure, thumidity, twspeed, twdirect, tprec]}
        tmp.update(ttmp)
    return tmp


def open_data(obj, type):
    # load data from file
    if type == "pickle":
        tmp = {}
        try:
            with open('weather.pickle', 'rb') as weatherFile:
                tmp = pickle.load(weatherFile)
        except FileNotFoundError:
            pass
        obj.update(tmp)

    elif type == "json":
        tmp = {}
        try:
            with open('weather.json', 'r') as weatherFile:
                tmp = json.load(weatherFile)
        except FileNotFoundError:
            pass
        converted_tmp = convert_to_normal_format(tmp)
        obj.update(converted_tmp)

    elif type == "yml":
        tmp = {}
        try:
            with open('weather.yml', 'rb') as weatherFile:
                tmp = yaml.load(weatherFile)
        except FileNotFoundError:
            pass
        obj.update(tmp)

    else:
        print("Format incorrect")


def save_data(obj, type):
    if type == "pickle":
        with open('weather.pickle', 'wb') as weatherFile:       # open file with data
            pickle.dump(obj, weatherFile)                       # save data
        print("Successfully saved.")

    elif type == "json":
        convertobj = convert_to_json_format(obj)
        with open('weather.json', 'w') as weatherFile:
            json.dump(convertobj, weatherFile)
        print("Successfully saved.")

    elif type == "yml":
        with open('weather.yml', 'w') as weatherFile:
            yaml.dump(obj, weatherFile)
        print("Successfully saved.")

    else:
        print("Format incorrect.")
