from Stack import Stack

def parantheses(expression):
	s = Stack()
	newexp = expression.split()
	balanced = True
	i = 0
	while i < len(expression) and balanced:
		character = expression[i]
		if character == "(":
#			print("found (")
			s.push(character)
		else:
			if s.isEmpty():
				print("I'm here")
				balanced = False
				print(balanced)
			else:
				s.pop()
		i += 1
	print(balanced, s.isEmpty())	
	if balanced and s.isEmpty():
		return True
	else:
		return False

def multparantheses(expression):
	s = Stack()
	newexp = expression.split()
	balanced = True
	i = 0
	while i < len(expression) and balanced:
		character = expression[i]
		if character == "(":
#			print("found (")
			s.push(character)
		else:
			if s.isEmpty():
				print("I'm here")
				balanced = False
				print(balanced)
			else:
				top = s.pop()
				if not matches(top, character):
					balanced = False
		i += 1
	print(balanced, s.isEmpty())	
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open,close):
	opens ="([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

print(parantheses("( ( (( ) ) ) "))
