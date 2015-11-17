import random

f = open('wordlist.txt', 'r')

secondWord = False
firstList = []
secondList = []

for line in f:
	if line == "!\n":
		secondWord = True
	elif secondWord:
		secondList.append(line.rstrip())
	else:
		firstList.append(line.rstrip())
firstIndex = random.randint(0, len(firstList)-1)
secondIndex = random.randint(0, len(secondList)-1)

if firstList[firstIndex] != "theory" and secondList[secondIndex] != "theory":
	print firstList[firstIndex] + ' ' + secondList[secondIndex] + " theory"
else:
	print firstList[firstIndex] + ' ' + secondList[secondIndex]