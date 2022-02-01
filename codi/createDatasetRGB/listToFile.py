import os

PATH_SD = 'C:/Users/ger-m/Desktop/UNI/4t/TFG/minidataset/sd/'

l = os.listdir(PATH_SD)

f = open("listfile.txt", 'w')

for el in l:
    f.write(el + '\n')
f.close()