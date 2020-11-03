
sally = "sally sells sea shells by the sea shore and by the road"
characters={}
for char in sally:
    if char in characters:
        characters[char]+=1
    else:
        characters[char]=1
charMax=min(characters.values())
for char in characters:
    if characters[char]==charMax:
        worst_char=char
        break
