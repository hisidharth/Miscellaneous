import random
animald={"bigcheese":["male","47","3'11","grey"],"jimothy":["male","17","7'11","green"],"smogon":["female","10","2'11","orange"],"ronathon":["female","49","6'1","black"],"jebidiah":["male","99","2'1","black"]}
alist=["bigcheese","jimothy","smogon","ronathon","jebidiah"]
schoice=random.choice(alist)

schoicegender=animald[schoice][0]
schoiceage=animald[schoice][1]
schoiceheight=animald[schoice][2]
schoicehair=animald[schoice][3]
index=0

while index<2:
    option=input("what will u do")
    option=option.lower()
    if option=="list":
        print(animald)
    elif option=="age":
        print(schoiceage)
        index+=1
    elif option=="height":
        print(schoiceheight)
        index+=1
    elif option=="gender":
        print(schoicegender)
        index+=1
    elif option=="hair":
        print(schoicehair)
        index+=1
guess=input("who are you guessing")
if guess==schoice:
    print("yes the correct answer was", schoice,".")
else:
    print("incorrect")
    index==4
        
        
        
        
