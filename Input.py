import datetime


def get_date():
    # input date
    while True:
        try:
            year = int(input('Enter date (year): '))
            month = int(input('Enter date (month):'))
            day = int(input('Enter date (day):'))
            tmp = datetime.date(year, month, day)           # chack date
        except ValueError:
            print('Values is not correct. Try again.')
            continue
        return tmp


def get_temp():
    # input temperature
    while True:
        try:
            tmp = int(input('Enter Temperature (eg. +8): '))
        except ValueError:                                  # chack temperature
            print('Values is not correct. Try again.')
            continue
        return tmp


def get_humidity():
    # input humidity
    while True:
        try:
            tmp = int(input('Enter humidity (%): '))
        except ValueError:                                  # chack huminidy
            print('Values is not correct. Try again.')
            continue
        if 0 <= tmp <= 100:
            return tmp
        else:
            print('Values is not correct. Try again.')


def get_preasure():
    # input preasure
    while True:
        try:
            tmp = int(input('Enter preasure (mm): '))
        except ValueError:                              # chack preasure
            print('Values is not correct. Try again.')
            continue
        return tmp


def get_wspeed():
    # input wind speed
    while True:
        try:
            tmp = float(input('Enter wind speed (m/sec): '))
        except ValueError:                              # chack wind speed
            print('Values is not correct. Try again.')
            continue
        return tmp


def get_year():
    while True:
        try:
            tmp = int(input('Enter year: '))
        except ValueError:
            print('Values is not correct. Try again.')
            continue
        if 0 <= tmp <= 2016:
            return tmp
        else:
            print('Values is not correct. Try again.')


def get_month():
    while True:
        try:
            tmp = int(input('Enter month: '))
        except ValueError:
            print('Values is not correct. Try again.')
            continue
        if 1 <= tmp <= 12:
            return tmp
        else:
            print('Values is not correct. Try again.')


def get_choice():
    while True:
        try:
            tmp = int(input())
        except ValueError:
            print('Choice is not correct. Try again.')
            continue
        return tmp
