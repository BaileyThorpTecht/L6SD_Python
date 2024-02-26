# Correct each program

# Program 1
#added an input and called the function
def greet(name):
    print("Hello, " + name + "!")

s = input("Enter a name:")
greet(s)

# Program 2
#y = "10"  ==>  y = 10
x = 5
y = 10
result = x + y
print("Result:", result)

# Program 3
#made it return area instead of nothing
#added an input and called function
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

r = int(input("Enter a radius:"))
print("area: " + str(calculate_area(r)))

# Program 4
#used == instead of =
number = input("Enter a number: ")
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Program 5
#c + d  ==>  a + b
#did not add input or call function, I think its not part of the challenge
def add_numbers(a, b):
    return a + b

# Program 6
#def print_message():  ==>  def print_message(message):
def print_message(message):
    print(message)

# Program 7
# replaced 'list' with the name of the list (numbers)
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print("Average:", average)

# Program 8
#indent print(i)
for i in range(5):
    print(i)

# Program 9
#typo
def multiply(a, b):
    result = a * b
    return result

# Program 10
#indent the prints
def check_temperature(temp):
    if temp > 30:
        print("It's hot outside.")
    else:
        print("It's cool outside.")
