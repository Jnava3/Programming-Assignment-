"""  John Nava
     Program #4
     COSC 1306
     Fall 2019
"""
def readArray(emArray, itemsNum):
    emArray=[]
    for i in range(itemsNum):
        aElement=int(input("Array["+ str(i)+"]"+" = "))
        emArray.append(aElement)   
    print("\nArray = " + str(emArray))
    return emArray

def maxValue(a):
    maxV=-100000
    for i in range(len(a)):
        if a[i]>maxV:
            maxV = a[i]
            i= i+1
    print("Max = " + str(maxV))
        
def minValue(b):
    minV=10000
    for i in range(len(b)):
        if b[i]<minV:
            minV = b[i]
            i= i+1
    print("Min = " + str(minV))

def numPositives(p):
    pos=0
    for i in range(int(len(p))):
        if p[i] >= 0:
            pos= pos+1
    print("Number of positives values = "+ str(pos)) 

def numNegatives(n):
    neg=0
    for i in range(int(len(n))):
        if n[i] < 0:
            neg = neg + 1 
    print("Number of negatives values = "+ str(neg))      

def average(avgArray):
    total= 0
    count=0
    for i in range(len(avgArray)):
        total= total + avgArray[i]
        count= count+1
    avg = total/count
    print("Average =", "{0:.2f}".format(avg))

array1=[]
iNum= int(input("Enter the size of the array: "))
array1 = readArray(array1,iNum)
maxValue(array1)
minValue(array1)
average(array1)
numPositives(array1)
numNegatives(array1)
