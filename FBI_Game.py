# FBI_the_Game.py

# This python program(app)asks user to guess where the bones are by inputting the row and colum index of the bone cells(e.g 2 5).
# and display the backyard to the user whether or not he/she hit the bone(show B at the particular bone cell)

# Suhua Qin, Nourham 
# November 27, 2015


# For bonus mark (check if a whole bone is found, if yes, tell the user what the bone number is)
def CheckBoneFound(rowIcolI):
    for i in range(len(datalist1)):
        if rowIcolI == datalist1[i]:
            datalist2[i][1] = 1
            match = datalist2.count(datalist2[i])
            BoneNumber = datalist2[i][0]
            if match == BoneL:
                print("Well done! A whole bone #", BoneNumber,"is found.")

# Display the backyard grid to the user
def display_backyard():
    print("\nThere are %i bones, each are %i cells long, buried in this backyard! Can you find them?" %(N_Bones,BoneL))
    for i in range(width):
        if i<10:
            print(i, end='  ')
        else:
            print(i, end=' ')  
    print()
    for i in range(height):
        for t in range(width):
            print(backyard[i][t],end ='  ')
        print(i)
# 
# Main
#
line1 = []  
datalist1 = []
datalist2 = []
xylist = []
#
# Read in data file
#
datafile = open('FBI_the_Game_Data_2.txt', 'r') 
datalist0 = list(datafile) 
#
# Read in first line
#
newL = datalist0[0].split() # newL stands for new line, it process   
line1.append(newL)      
width = int(line1[0][0])
height = int(line1[0][1])   
N_Bones = int(line1[0][2]) # N_Bones stands for number of bones  
BoneL = int(line1[0][3])   # BoneL stands for bone length
#
# create the data lists
#
for i in range(1,len(datalist0)):
    newL = datalist0[i].split()    
    for t in range(0,len(newL),2):
        xylist = [int(newL[t]),int(newL[t+1])]  
        datalist1.append(xylist)        # stuff it into datalist1
        datalist2.append([i,0])
        
backyard = [['.']* width for i in range(height)] #create the backyard list
#
# Interact with users
#
userInput = ""
print("Welcome to Fast Bone Investigation (FBI) the game.\nIn this game, we dig out bones from Mrs. Hudson\'s backyard!")
while userInput  != "-1":
    display_backyard()
    print("\nTo do so, please, enter the row and the column number of a cell in which you suspect a bone is buried", end = "")
    print("(e.g., 0 3 if you suspect that part of a bone is buried on the first row at the 4th column.")
    userInput = input("Enter -1 to quit : ")
    if userInput != "-1":
        trimmed = userInput.strip()         
        inputList1 = trimmed.split()
        if len(inputList1) == 0:
            print("***You have not entered anything. You need to enter a valid row and the column number!\n")
            
        elif len(inputList1) == 1 and userInput.isdigit():
            print("***You have entered only 1 value. You need to enter a valid row and the column number!\n")
            
        elif userInput.isalpha():
            print("***You have entered %s. You need to enter a valid row and the column number!"%userInput)
           
        else:
            rowI = int(inputList1[0])    #rowI stands for row index
            colI = int(inputList1[1])    #colI stands for colum index
            inputList2 = [rowI,colI]
            if rowI < 0 or rowI > height or colI < 0 or colI > width:
                print("You needed to enter a row and column number of a cell that is within the backyard!\n")
            
            else:
                if inputList2 in datalist1: # Check if user's input matches any bone cell(s)
                    print("\n****HIT!!!!****\n")
                    backyard[rowI][colI] = 'B'
                    CheckBoneFound(inputList2)
                    
                else:
                    print("\n****OOPS! MISSED!****\n")

        
else:
    print("Wasn't it fun! Bye!")
