my_dict = {}
with open('point_system', 'r') as f:
	#THIS IS A BLOCK
	for line in f:
		#print(char):
		letter = line.rstrip().lower()
		value = int (f.readline().rstrip())
		my_dict[letter] = value

word = input("Enter a word\n").lower()
total_points = 0
for i in word:
	total_points += my_dict[i]
print(total_points)