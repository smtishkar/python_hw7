# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
# имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv

from os import getcwd, listdir, path, rename
from pathlib import Path


def rename_function(wanted_name="video", count_nums=3, extension_old=".txt", extension_new=".csv", wanted_range=[3, 6]):
    count = 1
    temp = ''
    ZERO = '0'
    # print(listdir())
    for file in listdir():
        file_name, file_extention = path.splitext(file)
        if file_extention == extension_old:
            for i in range(count_nums-len(str(count))):
                temp += ZERO
            new_count = temp+str(count)
            rename(file, file_name[wanted_range[0]:wanted_range[1]
                                   ] + wanted_name+f'{new_count}'+extension_new)
            temp = ''
            count += 1


print(listdir())
rename_function(wanted_name="-hello-", count_nums=5,
                extension_old=".txt", extension_new=".jpg", wanted_range=[1, 6])
print(listdir())
