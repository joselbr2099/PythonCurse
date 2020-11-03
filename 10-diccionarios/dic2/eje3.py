str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words={}
for char in str1.split():
    if char in freq_words:
        freq_words[char]+=1
    else:
        freq_words[char]=1
