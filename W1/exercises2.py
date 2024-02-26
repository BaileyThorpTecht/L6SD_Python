def ex1():
    name = input()
    print("Hello " + name + ", nice to meet you")

def ex2():
    print("Enter two numbers:")
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2
    print("The sum is " + sum)

def ex3():
    print("Enter your favourite color:")
    color = input()
    print("Your favourite color is " + color)

def ex4():
    print("Here is the first message")
    print("Here is another")

def ex5():
    name = "name"
    age = "age"
    print("Your name is " + name + " and are " + age + " years old")

def ex6():
    i = 0
    while i < 5:
        i += 1
        print("Hello")

def ex7():
    print("Enter two strings:")
    s1 = input()
    s2 = input()
    (s1, s2) = (s2, s1)
    print(s1 + " " + s2)

def ex8():
    print("Enter two strings:")
    s1 = input()
    s2 = input()
    conc = s1 + s2
    print(conc)

def ex9():
    age = 19
    print(age)

def ex10():
    print("Enter two numbers:")
    num1 = int(input())
    num2 = int(input())
    print("Enter an operator: + - * /")
    op = input()
    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    elif op == "*":
        answer = num1 * num2
    elif op == "/":
        answer = num1 / num2
    print(answer)  

def ex11():
    print("Enter two numbers:")
    num1 = int(input())
    num2 = int(input())
    if num1 == num2:
        print("Numbers are equal")
    else:
        print("Not equal numbers")

def ex12():
    print("Enter two strings:")
    print(input() + input())

def ex13():
    print("Enter your age:")
    age = int(input())
    if age >= 18:
        print("Old enough to vote")
    else:
        print("Too young to vote")

def ex14():
    print("Enter a number")
    num = int(input())
    if num > 0:
        print("Number is positive")
    elif num == 0:
        print("Number is zero")
    elif num < 0:
        print("Number is negative")

def ex15():
    i = 0
    while i < 10:
        i += 1
        print(i)




#code starts here
activeExercise = int(input()) - 1
exList = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12, ex13, ex14, ex15]
exList[activeExercise]()
input()