"""  John Nava
     Program #5
     COSC 1306
     Fall 2019
"""
prizes = {"red": "a pencil", "blue": "a notebook", "green": "a t-shirt", "yellow": "a television", "gold": "a car"}

def compareTic(ticInput,lines,prizeList):
    award_given = False   
    for n in lines: 
        if n == ticInput: 
            print("A gold ticket was awarded.")
            prizeList.append("gold")
            award_given = True

        elif n[:4] == ticInput[:4]: 
            print("A yellow ticket was awarded.")
            prizeList.append("yellow")

            award_given = True
        elif n[:3] == ticInput[:3]: 
            print("A green ticket was awarded.")
            prizeList.append("green")

            award_given = True
        elif n[:2] == ticInput[:2]: 
            print("A blue ticket was awarded.")
            prizeList.append("blue")
  
            award_given = True
        elif n[:1] == ticInput[:1]: 
            print("A red ticket was awarded.")
            prizeList.append("red")
          
            award_given = True
    if(award_given == False):
        print("No tickets rewarded because of no matches.")

FileName = input('Enter the file name: ')
fp = open(FileName,'r')
userfile = fp.readlines()
lines = [n.rstrip('\n') for n in userfile]

LottList = [] 

userInput =input(' Enter in your first lottery ticket: ')
compareTic(userInput,lines,LottList)
    
userInput =input('Enter in your second lottery ticket: ')
compareTic(userInput,lines,LottList)

userInput =input('Enter in your third lottery ticket: ')
compareTic(userInput,lines,LottList)

print("Here are your prizes!")
for n in LottList: 
    print(n + " ticket:" +" you won", prizes[n]+ "!")


fp.close()
