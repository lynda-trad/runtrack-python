# Fizzbuzz
num = 1

while num <= 100:
    if num % 3 == num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    num += 1
