import datetime
import Open_file
import Input
import Configs
from dateutil import parser

weather = {}


def push_data():
    d1 = datetime.date(2015, 10, 10)
    d2 = datetime.date(2015, 10, 12)
    tmp = {d1: ['+10', 750, 48, 3.0, 'W', 'None'],
           d2: ['+8', 747, 53, 3.3, 'SW', 'None']}
    weather.update(tmp)


def test():
    # push_data()
    Open_file.open_data(weather, Configs.get_type())
    for i in weather:
        tmp = parser.parse(i)
        print(tmp.year)


def add_data():
    date = Input.get_date()
    temp = Input.get_temp()
    preasure = Input.get_preasure()
    humidity = Input.get_humidity()
    wspeed = Input.get_wspeed()
    wdirect = input('Enter wind direction (eg. SW or S): ')
    prec = input('Enter precipitations (eg. Rain or Snow): ')
    tmp = {date: [temp, preasure, humidity, wspeed, wdirect, prec]}
    weather.update(tmp)                                         # rewrite data that already exsist
    Open_file.save_data(weather, Configs.get_type())                                # save changes in file
    input('Press Enter to continue...')


def rm_data():
    date = Input.get_date()
    if date in weather:
        del weather[date]
        Open_file.save_data(weather, Configs.get_type())            # save changes in file
        input('Press Enter to continue...')
    else:
        input('Day in diary not found. Press Enter to continue...')
