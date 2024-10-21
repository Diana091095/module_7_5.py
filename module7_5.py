import os
import time

# a = os.getcwd() #путь до директории
# b = r'module7_5'
#
# target_dir = os.path.join(a, b)# Полный путь к целевой директории

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        filepath = os.path.join(root, file) # Полный путь к файлу
        filetime = os.path.getmtime(filepath)  # Время изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)  # Размер файла
        parent_dir = os.path.dirname(filepath)  # Родительская директория для файла
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,\n'
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
