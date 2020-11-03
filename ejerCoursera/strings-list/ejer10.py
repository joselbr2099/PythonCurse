stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro=""
#print(org.split(" "))
for word in sent.split(" "):
    if word not in stopwords:
        acro+=word[0].upper()+word[1].upper()+". "
#jjacro.pop()

print(acro)


