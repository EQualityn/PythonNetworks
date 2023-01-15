# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
options = ['unicast',
   'multicast',
   'local broadcast',
   'unassigned',
   'unused']


is_not_correct_ip = True
while is_not_correct_ip:
   ip = input("Input ip address ")
   ip = [byte for byte in ip.split('.')]
   if (len(ip) != 4 or not all(elem.isdigit() for elem in ip) or not all(int(elem)>=0 and int(elem)<=255 for elem in ip)):
      print("Неправильный IP-адрес")
      continue
   is_not_correct_ip = False

ip = [int(byte) for byte in ip]
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