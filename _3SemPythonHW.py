from random import randint
#Решение оформлять в виде функций
#По возможности добавляйте docstring
#1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def SumOfOddNumbers(List)->int: 
    """считает сумму чисел на нечетных позициях"""
    sum=0 
    for i in range(len(List)): #проходится до указанной цифры, не включая эту цифру
        if i%2 != 0: #ищем нечетную позицию
            sum=sum+List[i] #складываем
    return sum

list=[2,3,5,9,3]
print(f'text->{SumOfOddNumbers(list)}')

#2-Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]



def get_numbers(n, first, last):
    return [randint(first, last) for i in range(n)]

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

mylist = get_numbers(8, 2, 11)
print(mylist, end =' ')
print(' => ',pairs_mult(mylist))


#3-Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#[4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


def result(num):
    new_nums=[]
    s_num=len(nums)
    for i in range(s_num):
        new_nums.append(nums[i]-int(nums[i]))
    myMax = 0
    myMin = 0

    for i in range(N):
        if new_nums[i] > new_nums[myMax] : myMax=i
        if new_nums[i] < new_nums[myMin] : myMin=i
    print ( round(new_nums[myMax] - new_nums[myMin],2))
N=5 # Количество цифр для сравнения

nums = [1.1, 1.2, 3.1, 5.17, 10.02]
print (nums)
result(nums)

#4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
#Подумайте, как это можно решить с помощью рекурсии.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10
l = []
def convert(b):
    if (b == 0):
        return l
    dig = b % 2
    l.append(dig)
    convert(b // 2)
a = int(input("input number: "))
convert(a)
l.reverse()
print("binary form number:")
for i in l:
    print(i)
#5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fibonacci(n):
    if n in (0,1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("input a number term sequence:"))
print("term sequence Fibonacci:")
x=n-1
while x:
    print(f'-{fibonacci(x)}',end=' ')
    x-=1
for i in range(n):
    print(fibonacci(i),end=' ')
print()