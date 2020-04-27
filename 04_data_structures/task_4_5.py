# -*- coding: utf-8 -*-
'''
Задание 4.5
Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.
Результатом должен быть список: ['1', '3', '8']
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

com1One = command1.find("1")
com2One = command2.find("1")
command1 = command1[com1One : ]
command2 = command2[com2One : ]

com1 = command1.split(",")
com2 = command2.split(",")

com1 = set(com1)
com2 = set(com2)
res = com1 & com2
res = sorted(res)
print(res)
