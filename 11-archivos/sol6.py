openFile=open('emotion_words.txt')
emotions=list()
for line in openFile.readlines():
    emotions.append(line.split(" ")[0])
