# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
options = ['unicast',
   'multicast',
   'local broadcast',
   'unassigned',
   'unused']
ip = input("Input ip address ")
ip = [int(byte) for byte in ip.split('.')]
if (ip[0] >= 1 and ip[0] <= 223):
   print (options[0])
elif (ip[0] >= 224 and ip[0] <= 239):
   print(options[1])
elif (ip[0] == 255 and ip[1] == 255 and ip[2] == 255 and ip[3] == 255):
   print(options[2])
elif (ip[0] == 0 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0):
   print(options[3])
else: 
   print(options[4])