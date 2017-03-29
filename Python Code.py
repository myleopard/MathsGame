from random import randint, choice, sample
from time import time
questions = int(input("How many questions: "))
year = int(input("What year of school are you in: "))
correct = 0
start = time()
operatorsList = ["numbers","multiples","more","less","order","+","-","bonds"]
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
writingMax = 20
multiples = [2, 5, 10]
moreLess = [1]
maxCountingNumber = 10
maxSecondNumber = 10
bonds = 20
if year >= 2:
    operatorsList += ["place value","*","/"]
    numbers += ["twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", "thirty-nine", "forty", "forty-one", "forty-two", "forty-three", "forty-four", "forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty", "fifty-one", "fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven", "fifty-eight", "fifty-nine", "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five", "sixty-six", "sixty-seven", "sixty-eight", "sixty-nine", "seventy", "seventy-one", "seventy-two", "seventy-three", "seventy-four", "seventy-five", "seventy-six", "seventy-seven", "seventy-eight", "seventy-nine", "eighty", "eighty-one", "eighty-two", "eighty-three", "eighty-four", "eighty-five", "eighty-six", "eighty-seven", "eighty-eight", "eighty-nine", "ninety", "ninety-one","ninety-two", "ninety-three", "ninety-four", "ninety-five", "ninety-six", "ninety-seven", "ninety-eight", "ninety-nine","one hundred"]
    writingMax = 100
    multiples += [3]
    moreLess += [10]
    maxCountingNumber = 100
    bonds = 100
    timesAndDivide = [2, 5, 10]
    placeValueMax = 2
for i in range(questions):
    operator = choice(operatorsList)
    answer = -1
    actual = -2
    print("\n")
    if operator == "numbers":
        actual = randint(1,writingMax)
        answer = int(input("Write this number in digit form '"+numbers[actual]+"': "))
    elif operator == "multiples":
        givenMultiples = randint(3, 9)
        changeBy = choice(multiples)
        sequence = [i for i in range(changeBy, changeBy * givenMultiples, changeBy)]
        actual = sequence[-1] + changeBy
        answer = int(input("What comes after these numbers: "+", ".join([str(i) for i in sequence])+": "))
    elif operator in ("more","less"):
        changeBy = choice(moreLess)
        number = randint(changeBy,100-changeBy)
        if operator == "more":
            actual = number + changeBy
        if operator == "less":
            actual = number - changeBy
        answer = int(input("What is "+str(changeBy)+" "+operator+" than "+str(number)+": "))
    elif operator == "order":
        nums = sample(list(range(maxCountingNumber)), 3)
        answer = int(input("Which is highest: "+", ".join([str(i) for i in nums])+": "))
        actual = max(nums)
    elif operator in ("+","-"):
        num1 = randint(1,maxCountingNumber)
        num2 = randint(1,maxSecondNumber)
        while num1 == num2:
            num1 = randint(1, maxCountingNumber)
        if num2 > num1:
            num2, num1 = num1, num2
        answer = int(input("What is "+str(num1)+" "+operator+" "+str(num2)+": "))
        actual = eval(str(num1)+operator+str(num2))
    elif operator == "bonds":
        num = randint(1,bonds)
        actual = bonds - num
        answer = int(input(str(num)+" + ? = "+str(bonds)+", What is ?: "))
    elif operator == "*":
        num1 = randint(1,10)
        num2 = choice(timesAndDivide)
        actual = num1 * num2
        answer = int(input("What is "+str(num1)+" * "+str(num2)+": "))
    elif operator == "/":
        num2 = choice(timesAndDivide)
        num1 = choice([i for i in range(num2, num2*12, num2)])
        answer = int(input("What is "+str(num1)+" / "+str(num2)+": "))
        actual = num1 / num2
    elif operator == "place value":
        num = randint(10**(placeValueMax-1),10**placeValueMax)
        place = randint(0, placeValueMax-1)
        answer = int(input("What number is in the "+str(10**place)+"s column of "+str(num)+": "))
        actual = int(str(num)[::-1][place])
    else:
        print(operator, "is an invalid operator, please ask an administrator for help")

    if answer == actual:
         print("Correct!")
         correct += 1
    else:
         print("Incorrect, correct answer is: ", actual)
totalTime = time()-start
print("\n\nTotal:",str(correct)+"/"+str(questions),"\nTotal Time:",str(round(totalTime,1)),"seconds\nAverage Time:",str(round(totalTime/questions, 2)),"seconds")
