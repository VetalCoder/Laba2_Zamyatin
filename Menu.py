import os
import W_diary
import Output
import Input


def clear():
    # clear desktop
    os.system('clear')


def print_menu():
    # run menu
    while True:
        clear()
        print('''      Weather diary

            1. Add/Edit Element
            2. Remove Element
            3. Show data
            4. Show data by month
            5. Exit
                      ''')
        ans = Input.get_choice()                # input menu key
        if ans == 1:
            W_diary.add_data()
        elif ans == 2:
            W_diary.rm_data()
        elif ans == 3:
            Output.show_data()
        elif ans == 4:
            Output.show_data_by_month()
        elif ans == 5:
            os._exit(1)
        else:
            print('Try again')
