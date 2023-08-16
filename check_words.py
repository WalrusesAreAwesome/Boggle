import string
toCheck = open("words.txt").read().split("\n")

letterNums = {
	"a": 8,
	"b": 3,
	"c": 3,
	"d": 4,
	"e": 10,
	"f": 2,
	"g": 2,
	"h": 0,
	"i": 0,
	"j": 0,
	"k": 0,
	"l": 0,
	"m": 0,
	"n": 0,
	"o": 0,
	"p": 0,
	"qu": 0,
	"r": 0,
	"s": 0,
	"t": 0,
	"u": 0,
	"v": 0,
	"w": 0,
	"x": 0,
	"y": 0,
	"z": 0
}
validWords = []
letts = set(string.ascii_lowercase)
#toCheck = ["help"]
for word in toCheck:
	valid = True
	for i,c in enumerate(word):
		if c == "q" and word[min(len(word)-1,i+1)] != "u":
			valid = False
		if len(set(c).intersection(letts)) != 1:
			valid = False
		if len(word) < 3:
			valid = False
	if valid:
		validWords.append(word)

with open("valid_words.txt", "w") as f:
	for i,word in enumerate(validWords):
		f.write(word)
		if i<len(validWords)-1:
			f.write("\n")

print(len(validWords))





























