openFile=open('school_prompt.txt')
three=list()
for line in openFile.readlines():
    three.append(line.split(" ")[2])
