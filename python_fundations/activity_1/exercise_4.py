def get_divisible_numbers(number, max_number):
    # Modify numbers to avoid infinity loops
    rate = abs(number)
    limit = abs(max_number)
    divisible_numbers = []

    # Obtención de los números divisibles calculando el siguiente número.
    while number <= limit:
        divisible_numbers.append(number)
        number += rate
    return divisible_numbers


print(get_divisible_numbers(7, 100))
