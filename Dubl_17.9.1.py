

array = input("Введите число через пробел:")
array_list = [int(i) for i in array.split()]
n_user = input("Введите число:")
n_user = int(n_user)
if n_user % 1 == 0:

    array_list.append(n_user)
    number_index = array_list.index(n_user)
    print("Индекс введенного числа:", number_index)
    print("Список до сортировки: ", array_list)

def n_sort(array_list):
    for i in range(len(array_list)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array_list)):
            if array_list[j] < array_list[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array_list[i], array_list[idx_min] = array_list[idx_min], array_list[i]
    return array_list

print("Список после сортировки:", n_sort(array_list))


def bi_search(a: int, array: list) -> int:
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left

print("Индекс введенного числа:", bi_search(n_user, array_list))

array_list.index(n_user, array_list.index(n_user) - 1, array_list.index(n_user) + 1)
print("Индекс соседних чисел:", array_list.index(n_user) - 1, array_list.index(n_user) + 1)



































