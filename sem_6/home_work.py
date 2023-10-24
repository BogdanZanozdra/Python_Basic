# 1

n = int(input('Enter a number \n'))
numbers = [i for i in range(-n, n + 1) ]
# for i in range(-n, n + 1):
#     numbers.append(i)
print(f'Список элементов от -n до n: \n {numbers}')



# 2

array_indexes = input('Enter indexes: ').split(' ')
array_indexes = list(map(lambda x: int(x), array_indexes))
# for i in range(len(array_indexes)):
#     array_indexes[i] = int(array_indexes[i])
print(f'Список индексов для умножения: \n {array_indexes}')



# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

arr = [1, 1, 2, 3, 4, 5, 5]
print(arr)
res_array = []
res_array = list(filter(lambda i: arr.count(i) == 1, arr))
# for i in arr:
#     if arr.count(i) == 1:
#         res_array.append(i)
print(f'Список неповторяющихся чисел: {res_array}')



# 4. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

simple_numbers = []
def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

simple_numbers = list(filter(lambda x: prime(x), range(1, 100)))
# for number in range(1,100):
#     if prime(number ):
#         simple_numbers.append(number)
        
# print(simple_numbers)    

n = int(input('Задайте натуральное число: '))
for i in simple_numbers[1:]:
    while n % i == 0:
        n = n / i
        print(i, end=' ')



# 5

array = [1.1, 1.2, 3.1, 10.01]
# for i in range(len(array)):
#     array[i] = round(array[i] % 1, 2)
array = list(map(lambda x: round(x % 1, 2), array))
print(array)
print(max(array) - min(array))

