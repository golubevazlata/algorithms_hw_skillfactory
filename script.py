numbers = [float(x) for x in input("Введите последовательность чисел через пробел: ").split()]
numbers.sort()
print("Отсортированная по возрастанию последовательность чисел: ", numbers)
print("Введите любое число, которое больше", numbers[0], "и меньше либо равно",
      numbers[len(numbers) - 1], ":")
num = float(input(""))
if num <= numbers[0] or num > numbers[len(numbers) - 1]:
    print("Введено число, не удовлетворяющее условию")
    exit()
left_ind = 0
right_ind = len(numbers) - 1
while True:
    middle_ind = int((left_ind + right_ind) / 2)
    if numbers[middle_ind] < num <= numbers[middle_ind + 1]:
        break
    if numbers[middle_ind] < num:
        left_ind = middle_ind
    if numbers[middle_ind + 1] >= num:
        right_ind = middle_ind

print("\nВ отсортированной последовательности найден элемент с индексом", middle_ind, "и значением",
      numbers[middle_ind])
print("удовлетворяющий одновременно двум условиям:")
print("1. значение найденного элемента", numbers[middle_ind], "меньше введенного числа", num)
print("2. значение следующего за ним элемента", numbers[middle_ind + 1], "больше или равно введенному числу", num)
