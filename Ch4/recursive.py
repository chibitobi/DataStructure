import turtle

def listsum(list):
	if len(list) == 1:
		return list[0]
	else:
		print(list[1:])
		return list[0] + listsum(list[1:])
		
				#this part truncates list

def reverseString(string):
	#what is base case? end of the string
	if len(string) > 1:
		#print(string[len(string)-1])
		return string[len(string)-1] + reverseString(string[:len(string)-1])
	else:
		return string[0]

def palindrome(string):
	#if item is 0 = palindrome
	#if item is 1 = palindrome
#	print(string[0], string[-1])
	if len(string) < 2:
		return True
	if string[0] != string[-1]:
		return False
#	print(string[1:-1])
	return palindrome(string[1:-1])

string = "hello"
print(string[0], string[-1], string[1], string[1:-1], string[:])		
print("h, o, e, ell, hello")
#print(listsum([1, 4, 5, 6, 7]))
print("reverse the string \"Hello\"", reverseString("Hello"))
print("palindrome check", palindrome("nommon"))

def tree(branchLen, t):
	if branchLen > 5:
		t.forward(branchLen)
		t.right(20)
		tree(branchLen-15,t)
		t.left(40)
		tree(branchLen-15,t)
		t.right(20)
		t.backward(branchLen)
def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("green")
	tree(75,t)
	myWin.exitonclick()

main()
