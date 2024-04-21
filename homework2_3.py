import random

def get_numbers_ticket(min, max, quantity):
     if not (1 <= min <= max <= 1000):
          return []

     if not (1 <= quantity <= (max - min + 1)):
          return []

     random_numbers = set()
     while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min, max))

     sorted_numbers = sorted(list(random_numbers))

     return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)