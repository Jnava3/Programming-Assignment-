"""  John Nava
     Program #5: The AnytoBase10 function with strings
     COSC 1306
     Fall 2019
"""
import string
def AnyToBase10(value,base):
    value = str(value)

    if (base == 2):
        BinaryToDec = int(value, 2)
        return(BinaryToDec)
    if(base == 4): 
        QuatToDec = int(value, 4)
        return(QuatToDec)
    if(base == 8):
        OctToDec = int(value,8)
        return(OctToDec)
    if(base == 16):
        HexToDec = int(value,16)
        return(HexToDec)

value = input("Enter the value: ")
base = int(input("Enter the base: "))
if(base <8):
    value2 = int(value)
    AnyToBase10(value2,base)
    print("The base", base, "value", value, "is equal to", AnyToBase10(value,base), "in base 10")
else:
    AnyToBase10(value,base)
    print("The base", base, "value", value, "is equal to", AnyToBase10(value,base), "in base 10")

