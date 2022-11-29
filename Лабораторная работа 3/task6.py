list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

value = list_numbers[0]   # присваиваем максимальному значение первого элемента
index = 0 # индекс максимального элемента - первый элемент

for i, current_value in enumerate(list_numbers):
    if current_value >= value: # сравниваем текущее значение из списка с максимальным
        value = current_value # записываем в переменную в случае выполнения условия
        index = i # записываем индекс

list_numbers[index], list_numbers[19] = list_numbers[19], value# меняем местами элементы

print(list_numbers)
