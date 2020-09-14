my_dict = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[]}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
with open('scrabble_words.txt', 'r') as f:
	#THIS IS A BLOCK
	for line in f:
		#print(char):
		line = line.rstrip()
		key = len(line)
		my_dict[key].append(line)

word = ""
def take_input():
	letter = input("Enter letter\n").lower()
	if letter not in letters:
		print("Invalid Input. Try Again\n")
		return take_input()
	return letter

print (len(word))

def check_loss(word1):
	if(len(word) >= 3):
		if (len(word) > 15):
			return False 
		elif word.upper() in my_dict[len(word)]:
			return False
	return True


player = 0

while (check_loss(word) == True):
	print("Player " + str(player%2 + 1))
	word += take_input()
	print(word)
	player+= 1

if(len(word) > 15):
	print("Both Lose!")
else:
	print("Player " + str(player%2 + 1) + " Wins!")


