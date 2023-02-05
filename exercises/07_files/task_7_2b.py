# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]
to_read = argv[1]
to_write = argv[2]


with open(to_read, 'r') as file, open(to_write,'w') as write:
    for line in file:
        to_print = True
        if line.startswith('!'):
            continue
        for word in ignore:
             if word in line:
                to_print = False
        if (to_print):
            write.write(line)

