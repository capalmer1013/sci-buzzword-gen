import random

f = open('wordlist.txt', 'r')

secondWord = False
firstList = []
secondList = []

for line in f:
	if line == "!\n":
		secondWord = True
	elif secondWord:
		secondList.append(line)
	else:
		firstList.append(line)
firstIndex = random.randint(0, len(firstList))
secondIndex = random.randint(0, len(secondList))

if firstList[firstIndex] != "theory\n" and secondList[secondIndex] != "theory\n":
	print firstList[firstIndex] + ' ' + secondList[secondIndex] + " theory"
else:
	print firstList[firstIndex] + ' ' + secondList[secondIndex]