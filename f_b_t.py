#Write function that filters input by data type and checks size of input.
def filter_me(val):

    #If integer >= 100, "That's a big number!".
    #If integer < 100, "That's a small number".
    if(isinstance(val,int)):
        if(val >= 100):
            print(str(val) + ": That's a big number!")
        else:
            print(str(val) + ": That's a small number")

    #If string and len >= 50, "Long sentence.".
    #If string and len < 50, "Short sentence.".
    elif(isinstance(val,str)):
        if(len(val) >= 50):
            print(str(val) + ": Long sentence.")
        else:
            print(str(val) + ": Short sentence.")
    
    #If list >= 10, "Big list!".
    #If list < 10, "Short list.".
    elif(isinstance(val,list)):
        if(len(val) >= 10):
            print(str(val) + ": Big list!")
        else:
            print(str(val) + ": Short list.")
    else:
        print("What?????????")

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
filter_me(sI)
filter_me(mI)
filter_me(bI)
filter_me(eI)
filter_me(spI)

sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
filter_me(sS)
filter_me(mS)
filter_me(bS)

aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,9,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
filter_me(aL)
filter_me(mL)
filter_me(lL)
filter_me(eL)
filter_me(spL)
