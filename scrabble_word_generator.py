my_dict = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[]}
with open('scrabble_words.txt', 'r') as f:
	#THIS IS A BLOCK
	for line in f:
		#print(char):
		line = line.rstrip()
		key = len(line)
		my_dict[key].append(line)

def alphabetize(word):
	ordered = ''.join(sorted(word))
	return ordered

letters = input("Input your letters:\n").lower()

letters = str(alphabetize(letters))
length = len(letters)
all_words = []

for i in my_dict[length]:
	a = alphabetize(i.lower())
	#print(a)
	if a == letters:
		all_words.append(i)

print(all_words)