import random
min = 1
max = 1000

def get_numbers_ticket(min, max , quantity):
    numbers = set()   # Множина
    while len(numbers) < max:  # Цикл,
        for i in range(quantity):
           numbers.add(random.randint(min, max))
        return list( numbers )

    
lottery_numbers_1 = get_numbers_ticket( 1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers_1)

lottery_numbers_2 = get_numbers_ticket( 1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers_2)