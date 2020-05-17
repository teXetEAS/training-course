# -*- coding: utf-8 -*-
"""
Задание 7.2a
Сделать копию скрипта задания 7.2.
Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

config = []
with open("config_sw1.txt") as file:
    for string in file:
        string = string.strip()
        if not string.startswith("!"):
            config.append(string)

for conf in config:
    for ign in ignore:
        if conf.count(ign) > 0:
            print(conf)