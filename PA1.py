""" 
John Nava
Assignment #1
COSC 1306 MW 1:00-2:30
Fall 2019
"""
#Insert Timestamps
TS1_H =int(input("Enter the number of hours of the first timestamp: "))
TS1_M =int(input("Enter the number of minutes of the first timestamp: ")) 
TS1_S =int(input("Enter the number of seconds of the first timestamp: "))

TS2_H = int(input("Enter the number of hours of the second timestamp: "))
TS2_M = int(input("Enter the number of minutes of the second timestamp: "))
TS2_S = int(input("Enter the number of seconds of the second timestamp: "))

#Finding the difference between the timestamps
TS1 = (TS1_H, TS1_M, TS1_S)
TS2 = (TS2_H, TS2_M, TS2_S)
Diff1= TS1[0] - TS2[0]
Diff2= TS1[1] - TS2[1]
Diff3= TS1[2] - TS2[2]

#Check inverse positive time
if(Diff1 <= 0): 
    Diff1= -Diff1
    Diff2= -Diff2
    Diff3= -Diff3
elif(Diff1 == 0 and Diff2 <= 0):
    Diff2= -Diff2
    Diff3= -Diff3
elif(Diff1 == 0 and Diff2 ==0 and Diff3 <= 0):
    Diff3= -Diff3

if(Diff3 < 0):
    Diff3= 60 + Diff3
    Diff2= Diff2-1 

if(Diff2 < 0):
    Diff1= Diff1-1
    Diff2= 60 + Diff2

#Display
TSDisplay= "Time between timestamps: " + str(Diff1) + " Hour(s) " + str(Diff2) + " Minute(s) " + str(Diff3) + " Second(s) "
print(TSDisplay)