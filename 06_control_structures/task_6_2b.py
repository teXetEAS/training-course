# -*- coding: utf-8 -*-
'''
Задание 6.2b
Сделать копию скрипта задания 6.2a.
Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


#user_ip_input = input("enter ip: ")
user_ip_input = "256.1.1.1"
ip_input = user_ip_input.split(".")
while True:
    try:
        ip = []
        for i in ip_input:
            ip.append(int(i))
            i = int(i)
            if i > 255:
                print("Неправильный IP-адрес1")
                break
        if ip[0] >= 1 and ip[0] <= 223:
            print("unicast")
        elif ip[0] >= 224 and ip[0] <= 239:
            print("multicast")
        elif user_ip_input == "255.255.255.255":
            print("local broadcast")
        elif user_ip_input == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
    except ValueError:
        print('Неправильный IP-адрес')
    else:
        print("Здарова еба")
        break
