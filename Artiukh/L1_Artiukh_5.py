'''
«5»: Заполните массив из 10 элементов случайными числами в
интервале [0,100] и подсчитайте отдельно среднее значение всех
элементов, которые <50, и среднее значение всех элементов,
которые ≥50.
Пример:
Массив:
3 2 52 4 60 50 1 2 60 58 6
Ср. арифм. элементов < 50: 3.000
Ср. арифм. элементов >=50: 56.000
'''
from random import randint
suma=0
suma1=0
c,c1=0,0
s=[randint(0,100) for x in range(10)]
for i in range(10):
	if s[i]<50:
		suma=suma+s[i]
		c+=1
	else:
		suma1=suma1+s[i]
		c1+=1

print('Массив: ',*s)
print('ср арифм элементов <50: ',suma/c)
print('ср арифм элементов >=50: ',suma1/c1)

