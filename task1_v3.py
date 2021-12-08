from math import sqrt
katet1= input('Введите через пробел катеты 1 ')
katet2= input('Введите через пробел катеты 2 ')
katet1=[int(i) for i in katet1.split()]
katet2=[int(i) for i in katet2.split()]
for i,(x,y) in enumerate(zip(katet1, katet2)):
   print(f'Треугольник {i+1} с катетами {x} и {y} имеет площадь {(x*y)/2} '
         f'и гипотенузу {round(sqrt(x**2+y**2), 2)}' )