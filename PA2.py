"""  John Nava
     Program #2: The Discount Calculator
     COSC 1306
     Fall 2019
"""

#Insert no. of items & original price
itemnum=int(input("Items being sold: "))
cost=float(input("Original Cost ($): "))

#If the total cost is greater than or equal to $200
if(float(cost) >= float(200) and int(itemnum) <= 3):
    disc= .3
if(float(cost) >= float(200) and itemnum > 3 < 6):
    disc= .45
if(float(cost) >= float(200) and itemnum >= 6):
    disc= .60

#Other If statements
if(float(cost) > 50 and float(cost) < 200):
    disc= .10
if(float(cost) <= 50):
    disc= 0

#Convert to percentage
perc= int(disc * 100)

#Calculate Final price
savings= (cost * disc)
fincost= float(cost-savings)

#Display discount and final cost
print("Discount Applied: " + str(perc) + "%")
print("Final Cost: $" + "{0:.2f}".format(fincost))