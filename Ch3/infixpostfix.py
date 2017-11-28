from Stack import Stack




def infixtopost(expression):
	stackopr = Stack()
	postfixopr = Stack()
	newExpr = list(expression)
#	print(newExpr)
	index = 0
	output = ""
	while index < len(expression): #traversing through expression
		if newExpr[index] == "(": #finidng left paranthese
			print("found (")	
		print(newExpr[index]) 
		
		
		if newExpr[index] == "*" or newExpr[index]== "/":
			stackopr.push(newExpr[index])
		elif newExpr[index] == "+" or newExpr[index] == "-":
			opr = stackopr.pop()
			postfixopr.push(opr)
			stackopr.push(newExpr[index])
			print("pushed", newExpr[index])
			print("current output is:", output)
		elif not newExpr[index] == " ":
			postfixopr.push(newExpr[index])
			print("current mid", newExpr[index])
			print("mid output", output)
		

	
		while not postfixopr.isEmpty():
			character = postfixopr.pop()
			output += character	
		#elif not stackopr.isEmpty():
		#	opr = stackopr.pop()
			#print(opr)

		index = index+ 1
	return output


exp = "A * B + C * D"

print(infixtopost(exp))
