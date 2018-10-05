
def hello_world():
    return 'hello world'

def is_divisible_by_three(number):
    if number % 3 == 0:
        return True
    else:
        return False

def is_divisible_by_five(number):
    if number % 5 == 0:
        return True
    else:
        return False


def fizzbuzz(number):
    if is_divisible_by_three(number) == True & is_divisible_by_five(number) == True:
        return "FizzBuzz"
    elif is_divisible_by_three(number) == True:
        return "Fizz"
    elif is_divisible_by_five(number) == True:
        return "Buzz"
    else:
        return number

for x in range(101):
    print fizzbuzz(x)

# can refactor to have implicit return and implicit true
