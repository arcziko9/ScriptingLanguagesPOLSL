#Zadanie 95
import re

try:
    inputFile = open("danezadanie95.txt", "r")
    content = inputFile.read()
    inputFile.close()
except IOError:
    print("Blad otwiernaia pliku")
    exit()

usedWords = []
count = []

for word in re.sub("[^\w]", " ", str(content)).split():
    if word not in usedWords:
        usedWords.append(word)
        count.append(1)
    else:
        count[usedWords.index(word)] += 1

for i in range(len(usedWords)):
    print("{:<20}".format(usedWords[i]) + " = " + str(count[i]))