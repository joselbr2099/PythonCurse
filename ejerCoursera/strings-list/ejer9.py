stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro=""
print(org.replace(",","").split(" "))
for word in org.replace(",","").split(" "):
    if word not in stopwords:
        acro+=word[0].upper()
print(acro)

#print(org)
