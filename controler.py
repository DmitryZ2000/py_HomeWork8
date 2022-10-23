import view
import model


def start():    
    exit = False
    my_db = {}
    new_dic = {}
    while not exit:
        get_command = view.control_panel()        
        if get_command == '1': my_db = model.generate_fb(view.get_db_len())
        elif get_command == '2': new_dic = model.read_file('phonebook.csv')
        elif get_command == '3': model.write_file(my_db, 'phonebook.csv')
        elif get_command == '4': model.find_name(new_dic, view.get_man_number())
        elif get_command == '5': model.print_db(my_db)
        elif get_command == '6': model.print_db(new_dic)
        elif get_command == '7': 
            print('Программа завершена корректно')
            exit = True
        else: print('Ввели не верную оманду')

