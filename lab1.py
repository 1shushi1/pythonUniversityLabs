#Exercise 1.
#Ask 3 questions about the name, surname and age, and at the end create a sentence with this information.
def ex1():
    name = input("Enter your name : ")
    surname = input("Enter your surname : ")
    age = input("Enter your age : ")
    print("Hello :", name, surname + ". Your age is :", age)
ex1()

#Exersise 2.
#Reverse to change Fahrenheit to Celsius.
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter fahrenheit you would like to convert : "))
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print(round(fahrenheit_to_celsius(), 2))

#Exercise 3.
#Convert to the Polish grading system.
def converter_to_polish_grade_sys():
    score = float(input("Enter your score to compare : "))
    if  score >= 90:
        grade = 5
    elif score >= 80:
        grade = 4
    elif score >= 70:
        grade = 4
    elif score >= 60:
        grade = 3
    elif score >= 50:
        grade = 3
    else: grade = 2
    return grade
print(converter_to_polish_grade_sys())


#Exercise 4.
#Change the code so that there are two inputs and the first number it can be devidet.
def checkerForDividableNum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second nubmer: "))
    if num1 % num2 == 0:
        print(num1, "is divisible by", num2)
    else : print(num1, "is not divisible by", num2)
checkerForDividableNum()

#Exercise 6.
#Add a check to see if a triangle can be drawn with the given sides.
def triangleSidesChecker():
    side1 = float(input("Enter a first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("The triangle can be drawn")
    else: print("The triangle cannot be drawn")
triangleSidesChecker()

#Exercise 7.
#Add a check to see if someone is trying to divide by zero, if so, give an appropriate message
def devisionByZeroChecker():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("You cannot divide by zero")
            return
    else:
        print("Invalid operation")
        return
    print("The result:", round(result, 2))
devisionByZeroChecker()
