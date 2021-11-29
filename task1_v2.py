from math import sqrt
katets= input('Введите длины катетов 1 и 2 по очереди через пробел ')
katets=[int(i) for i in katets.split()]
katet1=katets[0::2]
katet2=katets[1::2]
for i in range(len(katet1)):
   print(f'Треугольник {i+1} с катетами {katet1[i]} и {katet2[i]} имеет площадь {(katet1[i]*katet2[i])/2} '
         f'и гипотенузу {round(sqrt(katet1[i]**2+katet2[i]**2), 2)}')
