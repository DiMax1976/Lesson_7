# """Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками
# """Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в"""
# """проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:"""
# |--my_project
#    ...
#   |--templates
#   |   |--mainapp
#   |   |  |--base.html
#   |   |  |--index.html
#   |   | --authapp
#   |      |--base.html
#   |      |--index.html
#
# """Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в"""
# """родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные"""
# """ситуации; это реальная задача, которая решена, например, во фреймворке django."""


import os
import shutil

dir_list_new = {'my_project': ['mainapp', 'adminapp', 'authapp', {'templates': ['mainapp', 'authapp']},
                               {'vigor': ['mainapp2', 'mainapp3', 'authapp2', 'imperial']}]}


def save_file(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, 'w+', encoding='utf-8') as f3:
            print("Шаблон для копирования в наличии -", file_name)


def searh_files(path_templates, file_1, file_2):
    ROOT = os.path.dirname(__file__)
    # print ( path_templates )
    root_dir = './'
    for item in os.scandir(path_templates):
        # print ( item.name, item.is_dir () )
        if item.is_dir() == True:
            shutil.copy2(ROOT + '/' + file_1, path_templates + '/' + item.name)
            shutil.copy2(ROOT + '/' + file_2, path_templates + '/' + item.name)
            print('Файлы:', file_1, file_2, 'скопированы в папку', path_templates)


def make_dir_in_place_2(my_dir_list):  # скрипт создания папок
    ROOT = os.path.dirname(__file__)
    # print(ROOT)
    for key, value in my_dir_list.items():
        # print(key, value)
        dir_name = key
        dir_path = os.path.join(ROOT, dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            for it_file in value:
                if type(it_file) is dict:
                    for key, value in it_file.items():
                        dir_name_x = key
                        dir_path_x = os.path.join(ROOT + '/' + dir_name, dir_name_x)
                        if not os.path.exists(dir_path_x):
                            os.mkdir(dir_path_x)
                            for it_fil_2 in value:
                                os.mkdir(dir_path_x + '/' + it_fil_2)

                else:
                    os.mkdir(dir_path + '/' + it_file)
                # print(dir_path+'/'+it_file)
        else:
            shutil.rmtree(dir_path)


def search_templates(my_dir_list, dir_search):
    ROOT = os.path.dirname(__file__)
    for key, value in my_dir_list.items():
        dir_name = key
        for it_file in value:
            if type(it_file) is dict:
                for key, value in it_file.items():
                    dir_name_x = key
                    if dir_name_x == dir_search:
                        dir_path_x = os.path.join(ROOT + '/' + dir_name, dir_name_x)
                        if not os.path.exists(dir_path_x):
                            print('папка удалена')
                        else:
                            searh_files(dir_path_x, 'base.html', 'index.html')


# 1 создаем структуру папок в каталоге проекта
make_dir_in_place_2(dir_list_new)
# 2 Создаем шаблоны для копирования
save_file('base.html')  # создаю шаблон 1 если его нет
save_file('index.html')  # создаю шаблон 2 если его нет
# 3 Ищем templates  и вносим в папку templates - + копируем файлы base.html и index.html
search_templates(dir_list_new, 'templates')
