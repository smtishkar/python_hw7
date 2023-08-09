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

from os import getcwd,listdir,path,rename

# def rename_function(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", wanted_range=[3, 6]):



#Тут меняем расширение
# initial_name = 'test.txt'
# file_name, file_extention = path.splitext(initial_name)
# if file_extention == '.txt':
#     new_name = rename(initial_name,file_name+'.csv')
# print(listdir())


#тут меняем название файла
# num_count = 5
# wanted_name = 'video'
# initial_name = 'test.txt'
# count=125
# temp=''
# ZERO = '0'


# for i in range(num_count-len(str(count))):
#     temp += ZERO
# new_count=temp+str(count)

# file_name, file_extention = path.splitext(initial_name)
# new_name = rename(initial_name,wanted_name+f'{new_count}'+file_extention)
# print(listdir())


#Тут будем делать срез в имени
num_count = 5
wanted_name = 'video'
initial_name = 'test.txt'
count=125
temp=''
ZERO = '0'


for i in range(num_count-len(str(count))):
    temp += ZERO
new_count=temp+str(count)

file_name, file_extention = path.splitext(initial_name)
new_name = rename(initial_name,wanted_name+f'{new_count}'+file_extention)
print(listdir())