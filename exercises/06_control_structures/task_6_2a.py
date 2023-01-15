# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

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
ip = input("Input ip address ")
ip = [byte for byte in ip.split('.')]

if (len(ip) != 4 or not all(elem.isdigit() for elem in ip) or not all(int(elem)>=0 and int(elem)<=255 for elem in ip)):
       print("Неправильный IP-адрес")
else:
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

#       ip = input("Введите IP-адрес в формате x.x.x.x: ")
# octets = ip.split(".")
# valid_ip = len(octets) == 4

# for i in octets:
#     valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

# if valid_ip:
#     if 1 <= int(octets[0]) <= 223:
#         print("unicast")
#     elif 224 <= int(octets[0]) <= 239:
#         print("multicast")
#     elif ip == "255.255.255.255":
#         print("local broadcast")
#     elif ip == "0.0.0.0":
#         print("unassigned")
#     else:
#         print("unused")
# else:
#     print("Неправильный IP-адрес")