str1 = "peter piper picked a peck of pickled peppers"
freq={}
for char in str1:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
