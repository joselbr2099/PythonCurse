sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
auxSentence=sentence.split(" ")
same_letter_count=0
for word in auxSentence:
    if word[0]==word[len(word)-1]:
        same_letter_count+=1
print(same_letter_count)
