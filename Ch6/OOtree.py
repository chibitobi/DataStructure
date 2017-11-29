from Stack import Stack
from tree import createBinaryTree
class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.leftC = None
		self.rightC = None
		#initialize tree so that you have root
		#and right / left children will be empty at first

	def insertLeft(self, newNode):
		if self.leftC == None:
			#after checking left child is empty, you create new binary tree
			#which contains root node and you add new Binary tree on top of it
			self.leftC = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			#if leftC is NOT empty, then you simply will swap with it
			t.leftC = self.leftC
			self.leftC = t
	def insertRight(self, newNode):
		if self.rightC == None:
			self.rightC = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightC = self.rightC
			self.rightC = t
	def getRightC(self):
		return self.rightC
	def getLeftC(self):
		return self.leftC
	def setRootVal(self,obj):
		self.key = obj
	def getRootVal(self):
		return self.key

def ParseTree(expression):
	explist = expression.split()
	paranStack = Stack()
	expTree = BinaryTree('')
	paranStack.push(expTree)
	currentTree = expTree
	print(currentTree)
	for i in explist:
		if i == "(":
			#this condition checks for opening parantheses
			#and pushes the node into the left side to denote it as such
			currentTree.insertLeft('')
			paranStack.push(currentTree)
			currentTree = currentTree.getLeftC()
		elif i in ['+', '-','*','/']:
			#this condition checks for operators
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			paranStack.push(currentTree)
			currentTree = currentTree.getRightC()
		elif i not in ['+', '-', '*', '/' , ')', '(']:
			#this condition checks for operands
			#print(currentTree)
			print(i)
			currentTree.setRootVal(int(i))
			parent = paranStack.pop()
			currentTree = parent	
		else:
			print(expTree)
#			raise valueError
		
	return expTree
	
exp = "( 1 + 3 ) + 3"
pt = ParseTree(exp)
#Use hierarchy of tree to realize the expression tree                         
