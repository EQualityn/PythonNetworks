# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["alias", "duplex",  "configuration"]

with open('config_sw1.txt', 'r') as file:
    for line in file:
        to_print = True
        if line.startswith('!'):
            continue
        for word in ignore:
             if word in line:
                to_print = False
        if (to_print):
            print(line.strip('\n'))
        
                
        
                
