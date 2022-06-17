key = [
        ['A','B','C','D','E'],
        ['F','G','H','I','K'],
        ['L','M','N','O','P'],
        ['Q','R','S','T','U'],
        ['V','W','X','Y','Z']
]


#RULE 1: If both letters are the same (of only a single letter remains)
#Add 'X' as placeholder after first letter

key_matrix = key
print(key_matrix)

# this is the text we're going to encrypt
plaintext = "hidethegoldtree"
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
        b = 'x'
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
        plaintextpairs.append(a + 'x')
        i += 1

print(plaintextpairs)

