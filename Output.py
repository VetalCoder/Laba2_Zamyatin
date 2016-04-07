import W_diary
import Menu
import Input


def show_data():
    # show all data in our diary
    Menu.clear()
    print('Date\t\tTemp\tPreasure\tHumidity\tWind Speed\tWind Direction\tPrecipitation')
    count = 0
    for i in W_diary.weather:
        print(i.isoformat() + '\t' + str(W_diary.weather[i][0]) +
              '\t' + str(W_diary.weather[i][1]) + '\t\t' +
              str(W_diary.weather[i][2]) + '\t\t' +
              str(W_diary.weather[i][3]) + '\t\t' +
              str(W_diary.weather[i][4]) +
              '\t\t' + str(W_diary.weather[i][5]))
        count += 1
    if not count:
        print('Diary is empty')
    input('Press Enter to continue...')


def show_data_by_month():
    # show weather during chosen month
    Menu.clear()
    year = Input.get_year()
    month = Input.get_month()  # reading month number
    count = 0
    print('Date\t\tTemp\tPreasure\tHumidity\tWind Speed\tWind Direction\tPrecipitation')
    for i in W_diary.weather:                       # show all data about thise month that exsist in diary
        if (i.year == year) & (i.month == month):
            print(i.isoformat() + '\t' +
                  str(W_diary.weather[i][0]) + '\t' +
                  str(W_diary.weather[i][1]) + '\t\t' +
                  str(W_diary.weather[i][2]) + '\t\t' +
                  str(W_diary.weather[i][3]) + '\t\t' +
                  str(W_diary.weather[i][4]) + '\t\t' +
                  str(W_diary.weather[i][5]))
            count += 1
    if not count:
        print('Diary is empty')
    input('Press Enter to continue...')
