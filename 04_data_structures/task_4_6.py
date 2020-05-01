# -*- coding: utf-8 -*-
'''
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0' //не понятно что за via

ospf_route = 'O        10.0.24.0/24 [110/41] 10.0.13.3, 3d18h, FastEthernet0/0'
keys = ["Protocol:", "Prefix:", "AD/Metric:", "Next-Hop:", "Last update:", "Outbound Interface:"]

ospf_route = ospf_route.split()

result = ["{:<20} {}\n ".format(key, value)for key, value in zip(keys, ospf_route)]
print('\n'.join(result))
