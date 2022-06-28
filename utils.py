import random


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum :
            maximum = number
    return maximum
 

class Dice:
    def roll():
        first_digit = random.randint(1,12)
        second_digit = random.randint(1,12)
        return first_digit, second_digit



