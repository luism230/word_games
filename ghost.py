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


def check_loss(word1):
	if(len(word) >= 3):
		if (len(word) > 15):
			return False 
		elif word.upper() in my_dict[len(word)]:
			return False
	return True

def find_word(word1, desired_length):
		for i in my_dict[desired_length]:
			if i.lower().startswith(word1):
				word1 = i[0:len(word1) + 1]
				return word1.lower()
		if desired_length + 2 < 16:
			return find_word(word1, desired_length + 2)
		else:
			if bot_check_loss(word1) == False:
				return "Your word doesn't exist. I win"
			else:
				return "I surrender. Player 1 wins"

def bot_check_loss(word1):
	if len(word1) > 14:
		return False
	else:
		for i in my_dict[len(word1) + 1]:
			if i.lower().startswith(word1):
				word1 = 1[0:len(word1) + 1]
				word1 = word1.lower()
				
				return True
		count = 0
		for j in my_dict:
			if j > len(word1) + 1:
				for words in my_dict[j]:
					if words.lower().startswith(word1):
						count += 1
		if count > 0:
			return True
		return False




answer = ''
while answer != '1' and answer != '2':
	answer = input("Enter '1' or '2' Player\n")	

player = 0
if answer == '2':
	while (check_loss(word) == True):
		print("Player " + str(player%2 + 1))
		word += take_input()
		print(word)
		player+= 1

	if(len(word) > 15):
		print("Both Lose!")
	else:
		print("Player " + str(player%2 + 1) + " Wins!")
else:
	while check_loss(word) == True:
		print("Player " + str(player%2 + 1))
		if player%2 +1 == 1:
			word += take_input()
			print(word)
			player+= 1
		else:
			word = find_word(word, len(word) + 2)
			print(word)
			player += 1


