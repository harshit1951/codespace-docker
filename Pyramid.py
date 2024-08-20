for i in range(1,6):
    for j in range(1,6):
        if j <= 5-i:
            print(" ",end="") # end="" prevents line break 
        else:
            print("+ ",end="") 

    print() #will create line break
