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

#Тут меняем расширение
extension_old=".txt" 
extension_new=".csv"
# def rename_function(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", wanted_range=[3, 6]):
a= listdir
initial_name = 'test.txt'
file_name, file_extention = path.splitext(initial_name)
if file_extention == '.txt':
    new_name = rename(initial_name,file_name+'.csv')

# file_name = path.splitext(file_name)[0]+'.cvs'
# rename(file_name,'test.cvs')
print(listdir())
# print(file_name)
# print(file_extention)