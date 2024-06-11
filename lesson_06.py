#task_01


input_string = input("Введіть строку: ")

unique_chars = set(input_string)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)

#task_02

while True:
    word = input("Введіть слово, яке містить літеру 'h': ")
    if 'h' in word or 'H' in word:
        print("Дякую! Ви ввели правильне слово.")
        break
    else:
        print("Слово не містить літеру 'h'. Спробуйте ще раз.")

#task_03

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = [item for item in lst1 if isinstance(item, str)]

print(lst2)

#task_04

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num

print("Сума всіх парних чисел у списку:", sum_even)
