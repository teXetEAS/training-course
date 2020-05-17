# -*- coding: utf-8 -*-
'''
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#user_ip_input = input("enter ip: ")
user_ip_input = "10.1.1.11111"
ipOctet = user_ip_input.split(".")
if user_ip_input.count(".") < 3 and len(ipOctet) < 4:
    print("Неправильный IP-адрес")
else:
    ip = []
    for i in ipOctet:
        if int(i) < 0 and int(i) > 255:
            print(i)
            print("Неправильный IP-адрес")
        else:
            ip.append(int(i))
            print("cvdxcv")
            print(type(i))
'''''
    if ip[0] >= 1 and ip[0] <=223:
        print("unicast")
    elif ip[0] >= 224 and ip[0] <= 239:
        print("multicast")
    elif user_ip_input == "255.255.255.255":
        print("local broadcast")
    elif user_ip_input == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")

'''''