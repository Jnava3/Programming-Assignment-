"""  Your name here
     Program #3: The number base converter
     COSC 1306
     Fall 2019
"""

def Base10toAny(base10, cnum):
    answer = ""
    while (base10 != 0):
        remain = base10 % cnum
        base10 = base10 // cnum
        answer = str(remain) + answer
    return(answer)

def Checkbase(base):
    if (base == 2 or base == 4 or base == 6 or base == 8 or base == 16):
        return True
    else:
        return False

def anytoBase10(n, base):
    num = str(n)
    if (base == 2):
        BinaryToDec = int(n, 2)
        return(BinaryToDec)
    if(base == 4): 
        QuatToDec = int(n, 4)
        return(QuatToDec)
    if(baseFrom == 8):
        OctToDec = int(n,8)
        return(OctToDec)

baseFrom = int(input("Base of the original number: "))
baseTo = int(input("Base of the new number: "))

if not(Checkbase(baseFrom)) or not(Checkbase(baseTo)):
    print("Invalid base")
else:
    number = int(input("Enter the number: "))
    if baseFrom == 10:
        result = Base10toAny(base10, cnum)
        print("The decimal number", base10,
              "is equal to", result, "in base", cnum)
    else:
        result = anytoBase10(n, base)
        print("The base", base, "number", n,
              "is equal to", result, "in base 10")