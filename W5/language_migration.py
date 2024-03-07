import math

def Square(number):
    return number * number

def ConcatenateStrings(str1, str2):
    return str1 + str2

def CountVowels(input):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in input:
        if char in vowels:
            count += 1
    
    return count

def SumArray(numbers):
    total = 0
    for n in numbers:
        total += n
    
    return total

def PrintMultiples(n):
    for i in range(1,6):
        print(i * n, end=" ")
    
    print()

def GetDayOfWeek(day):
    pass
#idk

def FindMax(numbers):
    return max(numbers)

def CelsiusToFahrenheit(celsius):
    return (celsius * 1.8) + 32

def IsPrime(number):
    if number < 2:
        return False
    sqrt = int(math.sqrt(number))
    for i in range(2,sqrt + 1):
        if number % i is 0:
            return False
    
    return True

def ReverseWords(sentence):
    words = sentence.split(" ")
    words.reverse()
    return ' '.join(words)

        
    