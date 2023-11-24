def my_round(number):
    integer_part = int(number)
    decimal_part = number - integer_part

    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

def my_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers
my_list = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded_list = [my_round(number) for number in my_list]
sorted_list = my_sort(rounded_list)
print("Liste initiale :", my_list)
print("Liste arrondie et triée :", sorted_list)
