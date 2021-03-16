string = input("Введите числа через пробелов:")
my_list = list(map(int, string.split())) # cписок чисел
element =int(input("Введите любое число:"))

def sort(array): # функциия сортировки массива по возрастанию
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x

def binary_search(array, element, left, right): # функция поиска индекса введоного числа
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


sort(my_list)
ind = binary_search(my_list, element, 0, len(my_list))

if ind == 0:
    print("Нет элемента меньше введеного")
else:
    print("Позиция элемента, который меньше введенного Вами числа: ",ind - 1)
if ind == len(my_list)-1:
    print("Нет элемента больше введеного")
else:
    print("Позиция элемента, который больше или равен введенному Вами числу: ",ind + 1)