scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
auxScores=scores.split(" ")
a_scores=0
for num in auxScores:
    if int(num)>=90:
        a_scores+=1
print(a_scores)
