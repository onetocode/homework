import sys
import day_planner.storage
from day_planner import storage
import os.path as Path


def open_menu(caption_txt,actions_vac,extra_text_bottom=''):
    print(caption_txt)
    for key,value in actions_vac.items():
        print('{0}.  {1}'.format(value,key))
    print(extra_text_bottom)

def validate_answer(vac_of_actions, wrong_action_text):
    choice=input("\nВведите число: \t")
    if choice not in vac_of_actions.values():
        print(wrong_action_text)
        return None
    return choice

def make_event(answer, vac, extra_list=''):
    vac.get(answer)()

def show_all_tasks():
    with connect() as connection:
        rows = storage.return_all_rows(connection)
    for row in rows:
        print(row)
    return True

def add_task():
    new_task=input('введите новую задачу:\t')
    with connect() as connection:
        storage.add_task(new_task,connection)
        print('Новая задача "{0}" успешно добавлена'.format(new_task))
    return False

def make_exit():
    sys.exit()

def redact():
    try:
        id = input('Введите id задачи: ')
        with connect() as connection:
            old_text = storage.get_exist_task(connection, id)
            new_text = input('Как бы вы хотели переформулировать "{0}" ? '.format(old_text))
            if storage.set_new_text(connection,new_text,id):
                print("Задача успешно отредактирована! ")
    except:
        print('Такой задачи нет')

def finish():
    try:
        id = input('Введите id задачи: ')
        with connect() as connection:
            old_status = storage.get_status(connection,id)
            if old_status == 0:
                new_status = 1
                if storage.set_new_status(connection,new_status,id):
                    print("Вы успешно справились с данной задачей!")
            else:
                print("Данная задача уже завершена!")
    except:
        print('Такой задачи нет !!!')

def restart():
    try:
        id = input('Введите id задачи: ')
        with connect() as connection:
            old_status = storage.get_status(connection, id)
            if old_status == 1:
                new_status = 0
                if storage.set_new_status(connection, new_status, id):
                    print("Теперь Вы можете сделать задачу еще раз")
            else:
                print("Эта задача и так не сделана, сначала сделай - потом перезапускай")
    except:
        print('Такой задачи нет !!!')

def are_you_sure():
    decision=input("Вы уверены? Y/N")
    return True if decision=="Y" else False


def db_is_empty():
    with connect() as connection:
        rows = storage.return_all_rows(connection)
        return True if rows==[] else False



main_menu_dict={
    "Вывести список задач": '1',
    "Добавить задачу": '2',
    "Выход": '3'
    }

ext_menu_dict={
    "Отредактировать задачу": '1',
    "Завершить задачу": '2',
    "Начать задачу сначала": '3',
}

error_action_text= 'Несуществующее действие !'
cancel_edit_text= 'Отменить редактирование'
empty_list_txt='\nСписок дел пуст.\nПридуймайте дело.'
main_menu_caption='\nЕжедневник. Выберите действие:\n'
extra_menu_caption="----------------------------------------------"
extra_menu_bottom='(Отмена - любое другое)'

list_open_extra=['1']

main_menu_func={
        '1': show_all_tasks,
        '2': add_task,
        '3': make_exit
    }

extra_menu_func = {
        '1': redact,
        '2': finish,
        '3': restart,
    }


connect = lambda: storage.connect('day_planner')
def main():

    creation_schema = Path.join(Path.dirname(__file__) ,'resources', 'schema.sql')
    with connect() as connection:
        storage.initialize(connection, creation_schema)
        while True:
            open_menu(main_menu_caption,main_menu_dict)
            answer = validate_answer(main_menu_dict, error_action_text)
            if answer:
                make_event(answer, main_menu_func, list_open_extra)
                if answer in list_open_extra:
                    if not db_is_empty():
                        open_menu(extra_menu_caption,ext_menu_dict,extra_menu_bottom)
                        answer = validate_answer(ext_menu_dict, cancel_edit_text)
                        if answer:
                            make_event(answer, extra_menu_func)
                    else:
                        print(empty_list_txt)