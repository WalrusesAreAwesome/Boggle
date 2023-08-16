scoring = [1,1,2,3,5,11]

boardtxt = "ensaanbijvtypfin"
boardtxt = "nlmatnstlsukeedb"
board = []
boardletts = set()
for i in range(4):
	board.append([])
	for j in range(4):
		board[i].append(boardtxt[i*4+j])
		boardletts = boardletts.union(set(boardtxt[i*4+j]))
print(boardletts)
	

validWords = []
with open("valid_words.txt") as f:
	english = f.read().split("\n")
	for word in english:
		valid = True
		for c in word:
			if len(boardletts.intersection(set(c))) != 1:
				valid = False
		if valid:
			validWords.append(word)

for word in validWords:
	start = 

print(len(validWords))