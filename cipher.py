import numpy as np #We import a package called NumPy this helps with array manipulation
key = np.array([
        ['A','B','C','D','E'],
        ['F','G','H','I','K'],
        ['L','M','N','O','P'],
        ['Q','R','S','T','U'],
        ['V','W','X','Y','Z']])


#RULE 1: If both letters are the same (of only a single letter remains)
#Add 'X' as placeholder after first letter

print(key)
  
# this is the text we're going to encrypt
plaintext = "Hidethegoldentree".upper() #We automatically UPPERCASE it, to match the Matrix

#You may want to look at getting the program to ask for a string when you run it

# this is our text split up into pairs 
plaintextpairs = []
# this is our text encrypted (still in pairs)
ciphertextpairs = []



# the while loop goes through each letter of the plaintext checks 2 things:
i = 0
while i < len(plaintext):
    # a will be the next letter we're up to
    a = plaintext[i]
    # b will be whatever letter follows a
    b = ''

    # 1) here it's checking to make sure we're not at the end of the plaintext yet
    if (i + 1) == len(plaintext):
        #if we're at the end then we make b = x, so it'll be added onto the last letter
        b = 'X'
    else:
        #if we're at not the end then we make b = ( i + 1), which is the next letter after 'a'
        b = plaintext[i+1]

    # 2) here it's checking if 'a' and 'b' are the same letters
    if a != b:
        # if 'a' is not the same letter as 'b' then we make them a pair ['ab']
        plaintextpairs.append(a + b)
        i += 2
    else: 
        # if 'a' is the same letter as 'b' then we make 'a' and 'x' a pair instead ['ax']
        plaintextpairs.append(a + 'X')
        i += 1


print(plaintext)
print(plaintextpairs) 
coords=[] 
#This finds the co ordinates of our pairs
for i in plaintextpairs:
    #i[0] is the first digit of the pair and i[1] is the first digit of the pair
    coords.append([(str(np.argwhere(key == i[0]))), str(np.argwhere(key == i[1]))])
    #We convert to String (using str) to print to console
    # We use argwhere to find the x and y index of the letter
    # then we put this information into an array called coords

#Defining our Functions
def horizontal_shift(x1,y1,x2,y2): 
    x1 = int(x1)
    y1 = int(y1) 
    if (y1 == 4): #If it is at the end of the array horizontally, wrap it back to 0
        y1=0 
    else:
        y1 = y1 +1
    x2 = int(x2)
    y2 = int(y2)
    if (y2 == 4): #If it is at the end of the array horizontally, wrap it back to 0
        y2=0 
    else:
        y2 = y2 +1
    pair = key[x1][y1]+key[x2][y2]
    ciphertextpairs.append(pair)
 
def vertical_shift(x1,y1,x2,y2):
    x1 = int(x1)
    if (x1 == 4): #If it is at the end of the array vertically, wrap it back to 0
        x1=0 
    else:
        x1 = x1 +1
    y1 = int(y1) 

    x2 = int(x2)
    if (x2 == 4): #If it is at the end of the array vertically, wrap it back to 0
        x2=0
    else: 
        x2 = x2 + 1
    y2 = int(y2)
    pair = key[x1][y1]+key[x2][y2]
    ciphertextpairs.append(pair)

def box_shift(x1,y1,x2,y2):
    #To do the box shift, we simply just swap the Ys 
    x1 = int(x1)  
    y1 = int(y1) 
    x2 = int(x2)
    y2 = int(y2)
    pair = key[x1][y2]+key[x2][y1]
    ciphertextpairs.append(pair)

for i in coords: #We iterate over the coordinates and see where the letters are in the cipher
    #This checks if the rows of the two letters are the same
    if (i[0][2] == i[1][2]):
        horizontal_shift(i[0][2], i[0][4], i[1][2], i[1][4]) #We send the co ordinates to the horizontal function
    #Checks to see the columns of the two letters are the same
    elif (i[0][4] == i[1][4]):
        vertical_shift(i[0][2], i[0][4], i[1][2], i[1][4]) #We send the co ordinates to the vertical function
    #If neither row or column matches, the letters must be diagonally apart
    else:
        box_shift(i[0][2], i[0][4], i[1][2], i[1][4]) #We send the co ordinates to the box shift function
    
print(ciphertextpairs)    
