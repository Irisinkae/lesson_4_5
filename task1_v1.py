from math import sqrt
katet1= input('Введите через пробел катеты 1 ')
katet2= input('Введите через пробел катеты 2 ')
katet1=[int(i) for i in katet1.split()]
katet2=[int(i) for i in katet2.split()]
for i in range(len(katet1)):
   print(f'Треугольник {i+1} с катетами {katet1[i]} и {katet2[i]} имеет площадь {(katet1[i]*katet2[i])/2} '
         f'и гипотенузу {round(sqrt(katet1[i]**2+katet2[i]**2), 2)}' )

