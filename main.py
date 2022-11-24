import os

directory = 'human_decks'

decks = []
for file in os.listdir(directory):
    fileName = os.path.join(directory, file)
    cards = []
    if os.path.isfile(fileName):
        curFile = open(fileName, 'r')
        fileText = curFile.readlines()
        for line in fileText:
            contents = line.split()
            if len(contents) > 0:
                try:
                    num = int(contents.pop(0))
                except:
                    break
                card = " ".join(contents)
                for i in range(num):
                    cards.append(card)
        curFile.close()
    decks.append(cards)


for i in range(len(decks)):
    for card in decks[i]:
        for j in range(i+1, len(decks)):
            if card in decks[j]:
                decks[j].remove(card)
    print(decks[i], len(decks[i]))


cardlist = []
basicCount = [0,0,0,0,0]
basicTypes = ['Plains', 'Island', 'Swamp', 'Mountain', 'Forest']

for deck in decks:
    for card in deck:
        if card in basicTypes:
            basicCount[basicTypes.index(card)] += 1
        else: 
            cardlist.append(card)

cardlist.sort()

totalBasics = 0
for count in basicCount:
    totalBasics += count

writeFile = open(directory + "_compiled_cards.txt", 'w')

writeFile.write("Total cards: " + str(len(cardlist) + totalBasics) + "\n\n")

for i in range(5):
    if basicCount[i] > 0:
        writeFile.write(str(basicCount[i]) + " " + basicTypes[i] + "\n")

for card in cardlist:
    writeFile.write("1 " + card + "\n")
writeFile.close()







