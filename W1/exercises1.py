
def exercise_1():
    print("Enter a number:")
    try:
        num = int(input())
    except:
        print("not a number")
    else:
        if num % 2 == 0:
            print("even")
        else:
            print("odd")


def exercise_2():
    print("aw shucks")


def exercise_3():
    print("Enter your age:")
    num = int(input())
    if num >= 17:
        print("old enough to vote")
    else:
        print("too young to vote")

def exercise_4():
    num = 5 * 2 + 3
    print(num)
    #the answer should be 13
    #multiplication goes first, then addition
    #5 * 2 + 3
    #10 + 3
    #13


def exercise_5():
    def getNum():
        while True:
            try:
                n = int(input())
            except:
                print("You must enter a number")
            else:
                break
        return n
    
    def getOp():
        while True:
            s = input()
            if s == '+' or s == '-' or s == '*' or s == '/':
                break
            else:
                print("You must enter a valid operator: + - * /")
        return s

    #exercise_5 code starts
    print("Enter a number:")
    num1 = getNum()
    print("Enter one of the following operators: + - * /")
    op = getOp()
    print("Enter another number:")
    num2 = getNum()

    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2
    elif op == '/':
        if num2 == 0:
            answer = "cannot divide by 0"
        else:
            answer = num1 / num2
    
    print(answer)


#start of code
    
#exercise_1()
#exercise_2()
#exercise_3()
#exercise_4()
exercise_5()

input()
#end of code

