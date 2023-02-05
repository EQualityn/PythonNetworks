# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
file = open('ospf.txt', 'r')
params = ["Prefix", "AD/Metric","","Next-Hop", "Last update", "Outbound Interface"]

for line in file:
    line = line.strip('O \n').replace('[','').replace(']','').replace(',','').split(' ')
    print("{:25} {}".format(params[0],line[0]))
    print("{:25} {}".format(params[1],line[1]))
    print("{:25} {}".format(params[3],line[3]))
    print("{:25} {}".format(params[4],line[4]))
    print("{:25} {}".format(params[5],line[5]))
    print()