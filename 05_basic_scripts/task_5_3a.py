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
'''
modList = dict(access_template = access_template, trunk_template = trunk_template)

user_intf_mod = input("Укажите режим интерфейса (access/trunk): ")
user_intf_type = input("Укажите номер интерфейса: ")

inputMod = "{}_{}".format(user_intf_mod, "template")
reqestVlan = 

inputAccess = input("Укажите номер VLAN: ")
inputTrunk = input("Укажите разрешенные VLAN(s): ")

print("-"*30, "\nInterface {}".format(user_intf_type))

print("\n".join(modList[inputMod]).format(user_vlan))

print(london_co.get(inputParam, "Такого параметра нет"))

'''

