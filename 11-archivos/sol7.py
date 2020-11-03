openFile=open('school_prompt.txt')
p_words=list()
for line in openFile.readlines():
    for word in line.split():
        if 'p' in word:
            p_words.append(word)
