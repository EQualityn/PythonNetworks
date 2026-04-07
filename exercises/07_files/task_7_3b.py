# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('CAM_table.txt') as file:
    table = []
    for line in file:
        if 'DYNAMIC' in line:
            vlan, mac, port = line.replace('DYNAMIC', '').strip().split()
            vlan = int(vlan)
            table.append([vlan, mac, port])
table.sort()
vlan_input = int(input('Enter VLAN number: '))
for line in table:
        if line[0] == vlan_input:
            print(f"{line[0]:<10} {line[1]:<20} {line[2]}")