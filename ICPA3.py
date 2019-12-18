"""Your name here
In-class Program #3: The class average
COSC 1306
Fall 2019
"""

def readGrade():
    grade = int(input("Enter the grade: "))
    while grade < 0 or grade > 100:
        print("Invalid grade")
        grade = int(input("Enter the grade: "))
    return grade

stunum= int(input("Enter the number of students: "))
examnum = int(input("Enter the number of exams: "))

def examAverage(stunum, examnum):
    i=0 
    total= 0
    for i in range(stunum):
        total = readGrade() +total
    average = (total/stunum)
    return average

for i in range(1, examnum + 1):
    print("Enter the grades of exam "+ str(i) )
    x = examAverage(stunum, examnum)
    print("The average of exam " + str(i) + " is: {0:.2f}".format(x))

