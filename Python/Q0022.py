""" Project Euler Question 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""


def value(nameTested):
    name = nameTested.strip('\"')
    ret = 0
    for c in name:
        ret += ord(c) - ord('A') + 1
    return ret


file = open("p022_names.txt", 'r')
listOfNames = []
for line in file:
    listOfNames = line.split(',')
listOfNames.sort()
nameScore = 0
for i in range(0, len(listOfNames)):
    nameScore += value(listOfNames[i]) * (i + 1)
print(nameScore)
