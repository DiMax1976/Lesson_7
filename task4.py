import os


def statistic_files_in_place(my_dir_path):
    counter_100 = 0
    counter_1000 = 0
    counter_10000 = 0
    counter_100000 = 0
    if not os.path.exists(my_dir_path):
        print("Папка не существует!")
    else:
        for top, dirs, files in os.walk(my_dir_path):
            for nm in files:
                file_name = (os.path.join(top, nm))
                size_f = os.stat(file_name).st_size
                if size_f <= 100:
                    counter_100 = +1
                elif size_f <= 5000:
                    counter_1000 += 1
                elif size_f <= 10000:
                    counter_10000 += 1
                elif size_f <= 100000:
                    counter_100000 += 1
                elif size_f >= 100000:
                    counter_100000 += 1
    return {100: counter_100, 1000: counter_1000, 10000: counter_10000, 100000: counter_100000}


ROOT = os.path.dirname(__file__)
print(ROOT)
print(statistic_files_in_place(ROOT+'/'+'some_data'))
