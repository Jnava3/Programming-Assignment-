"""John Nava
In-class Program #1: The sum of natural numbers
COSC 1306
Fall 2019
This program computes the sum of the natural numbers from m to n (where m > 1 and n > m).
"""

#Inputs Collection
m=int(input())
n=int(input())

#Calculations
Sum1 = int(((n*(n+1))/2))
Sum2 = int(((m-1)*(m-1+1))/2)
Diff= Sum1 - Sum2
Sum3 = "The sum of the natural numbers from " + str(m) + " to " + str(n) + " is: "

#Answers
print(Sum3,Diff)



