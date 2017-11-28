from Deque import Deque


def palindrome(word):
	palqueue = Deque()

	splitword = list(word)
	print(splitword)
	for i in splitword:
		palqueue.addFront(i)
	palindrome = True
	while not palqueue.isEmpty() and palqueue.size() > 1 and palindrome:
		a = palqueue.removeFront()
		b = palqueue.removeRear()
		print(a,b)		
		if a == b:
			palindrome = True
		else:
			palindrome = False

	return palindrome

print(palindrome("radar"))
print(palindrome("raasdfr"))
