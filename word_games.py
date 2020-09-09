
def main():
	with open('names', 'r') as f:
		#THIS IS A BLOCK
		for line in f:
			print(line)
	#eEVERYTHING PAST HERE, THE FILE IS CLOSED
if __name__ == "__main__":
	main()