# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Задание 4.8
Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов
Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = '192.168.3.1'
ip = ip.split(".")
ip1[0] = ip[0]
ip2[1] = ip[1]
ip3[2] = ip[2]
ip4[3] = ip[3]

#ip10 = "{0:<10} {1:<10} {2:<10} {3:<10}".format(ip)
ip2 = "{0:010b} {1:010b} {2:010b} {3:010b}".format(ip1, ip2, ip3, ip4)

print(ip2)
#print(ip10)

#недаделано