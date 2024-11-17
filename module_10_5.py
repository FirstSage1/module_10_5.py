# module_10_5.py. "Многопроцессное программирование"
# =====================================================
'''Задача "Многопроцессное считывание"'''

# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.

import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as file1:
        while True:
            line = file1.readline().strip()
            all_data.append(line)
            if not line:
                break

# Создайте список названий файлов в соответствии с названиями файлов архива.
files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время
# выполнения и выведите его в консоль.
start1 = datetime.now()
for i in files:
    #print(i)
    read_info(i)
end1 = datetime.now()
time_of_line_function = end1 - start1
print(f'Время работы линейного вызова : {time_of_line_function}')

# Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
# контекстный менеджер with и объект Pool. Для вызова функции используйте метод map,
# передав в него функцию read_info и список названий файлов. Измерьте время выполнения
# и выведите его в консоль.
if __name__ == '__main__':
    start2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end2 = datetime.now()
    time_of_multiprocessing = end2 - start2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')

    # ----------------------------------------------------------------------
