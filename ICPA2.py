"""
John Nava
In-class Program #2: The Calculator
COSC 1306
Fall 2019
"""


#Enter inputs 
num1 = int(input("Enter the value of first number: "))
num2 = int(input("Enter the value of second number: "))

#Set equations
plus= int(num1 + num2) 
minus= int(num1 - num2)
mult= num1 * num2
div= float(num1 /num2)

operation = input("Enter the operation (+) = 1, (-) = 2, (*) = 3, (/) = 4: ")

if operation == '1':
    print("Result = ", plus)
elif operation == '2':
    print("Result = ", minus)
elif operation == '3':
    print("Result = ", mult)
elif operation == '4':
    print("Result = ", "{0:.2f}".format(div))
elif (num2 == '0' and operation == '4'):
    print("Division by zero")
else: 
    print("Invalid option")

