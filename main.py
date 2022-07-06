
import os
import shutil
import sys
from famous_persons import get_person_and_question
from wallet import personal_wallet

while True:
    print('1. Создать папку:')
    print('2. удалить (фаил/папку)')
    print('3. копировать (фаил/папку)')
    print('4. посмотреть содержимое рабочей дериктории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. посмотреть информацию об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10.мой банковский счет')
    print('11.выход')

    menu = input('Выберите пункт меню: ')

    if menu == '1': # создание папки
        new_folder = input('Назовите папку): ')
        print(os.mkdir(new_folder))
    elif menu == '2': # удаление папки
        del_folder = input('Удалить (папку/фаил): ')
        if os.path.isfile(del_folder) == True:
            print(os.remove(del_folder))
        if os.path.exists(del_folder) == True:
            print(os.rmdir(del_folder))
    elif menu == '3': # Копирование папки
        copy_folder = input('копировать (папку/фаил): ')
        copy_folder1 = input('назовите скопированную (папку/фаил): ')
        print(shutil.copy(copy_folder, copy_folder1))
    elif menu == '4': # посмотреть содержимое рабочей дериктории.
        print(os.listdir())
    # elif menu == '5': # просмотр папок.
    #     path = 'venv' #input('название папки: ')
    #     for folder in os.walk(path):
    #         print('Вложенные папки: ', folder)
    #         break
    #     directory = os.walk(path)
    #     print(next(directory))
    # elif menu == '6': # просмотр файлов.
    #     path = input('название папки: ')
    #     for files in os.walk(path):
    #         print('Файлы в папке: ', files)
    #         break
    elif menu == '7':
        print(sys.platform)
    elif menu == '8':
        command = "python --version"
        print(os.system(command))
    elif menu == '9': # викторина
        rounds = int(input('Сколько раз вы хотите играть?'))
        for i in range(rounds):
            get_person_and_question()
        print('Пока!')
    elif menu == '10': # кошелек
        personal_wallet()
    elif menu == '11': # Выход
        break
    else:
        print('Неверный пункт меню')
