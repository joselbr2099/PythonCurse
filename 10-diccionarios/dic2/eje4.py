sally = "sally sells sea shells by the sea shore"
characters={}
for char in sally:
    if char in characters:
        characters[char]+=1
    else:
        characters[char]=1
charMax=max(characters.values())
for char in characters:
    if characters[char]==charMax:
        best_char=char
        break
