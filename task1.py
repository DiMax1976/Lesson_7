"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:"""
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
import os
import shutil

dir_list_new = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_dir_in_place(my_dir_list):
    ROOT = os.path.dirname(__file__)
    for key, value in my_dir_list.items():
        # print(key, value)
        dir_name = key
        dir_path = os.path.join(ROOT, dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            for it_file in value:
                os.mkdir(dir_path + '/' + it_file)
                # print(dir_path+'/'+it_file)
        else:
            shutil.rmtree(dir_path)


make_dir_in_place(dir_list_new)
"""____________Гусь не сложный____________________________"""
