#!/usr/bin/python3
def fizzbuzz():
    sentence = ""
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            sentence += "FizzBuzz "
        elif number % 5 == 0:
            sentence += "Buzz "
        elif number % 3 == 0:
            sentence += "Fizz "
        else:
            sentence += str(number) + " "
    print(sentence, end="")
