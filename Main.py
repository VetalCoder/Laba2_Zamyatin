import Menu
import Open_file
import W_diary
import Configs


def main():
    Open_file.open_data(W_diary.weather, Configs.get_type())        # load data from file
    Menu.print_menu()                           # run menu

main()
