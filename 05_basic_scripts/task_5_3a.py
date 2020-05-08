# -*- coding: utf-8 -*-
'''
Задание 5.3a
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'
Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

user_intf_mod = input("Укажите режим интерфейса (access/trunk): ")
user_intf_type = input("Укажите номер интерфейса: ")

if user_intf_mod == "access":
    user_vlan = input("Укажите номер VLAN: ")
    print("-" * 30 + "\nInterface: " + user_intf_type)
    print("\n".join(access_template).format(user_vlan))
elif user_intf_mod == "trunk":
    user_vlan = input("Укажите разрешенные VELANs: ")
    print("-" * 30 + "\nInterface: " + user_intf_type)
    print("\n".join(trunk_template).format(user_vlan))
else:
    print("ERROR")

#ахуенный и пиздатый говнокод ебаный


