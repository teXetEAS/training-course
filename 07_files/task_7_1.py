# -*- coding: utf-8 -*-
'''
Задание 7.1
Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

conf = ["Protocol:", "Prefix:", "AD/Metric:", "хуйня:", "Next-Hop:", "Last update:", "Outbound Interface:"]

with open("ospf.txt") as fale:
    for param in fale:
        params = param.replace("[", "").replace("]", "").split()
        for vel in params:
            pass

result = ["{:<20} {}\n ".format(key, value)for key, value in zip(keys, ospf_route)]








'''
    for param in fale:
        params = param.replace("[", "").replace("]", "").split()
        for key in conf:
            print("*" * 50)
            for vel in params:
                    res = "{}{}".format(key, vel)
                    print(res)

           
            for key in conf:
                res = "{}{}".format(key, vel)
                print(res)
'''


#я хз кароч