

#this will be done recursively


myTree = ['a', #root
	['b', #left subtree start
	  ['d', [], []],
	  ['e', [], []] ], #left subtree end
	['c', #right subtree start
	  ['f', [], []],
	  [] ] 	 	   #right subtree end
	]

#notice how myTree[0] will be denoted as root
#	how myTree[1] will be denoted as left subtree
#	how myTree[2] will be denoted as right subtree

print('root = ', myTree[0])
print('left subtree = ', myTree[1])
print('right subtree = ', myTree[2])
#this is for basic testing


def createBinaryTree(r):
	return [r, [], []]
	#r = root, [] [] two empty sublists for children	

r = createBinaryTree(1)
#print(r)

def insertLeft(root, newValue):
	tree = root.pop(1)
	#pops the first element in [r, [], []] which is middle []
	#if this is empty, then tree is good to go and insert value
	#print(tree, len(tree))
	if (len(tree) < 1):
		#print("length less than 1")
		root.insert(1, [newValue, tree, []])
	else:
		root.insert(1, [newValue, [], []])
	return root

def insertRight(root, newValue):
	tree = root.pop(2)
	if (len(tree) < 1):
		#print("length less than 1")
		root.insert(2, [newValue, tree, []])
	else:
		root.insert(2, [newValue, [], []])
	return root
def getRootValue(root):
	return root[0]

def getleftChild(root):
	return root[1]

def getrightChild(root):
	return root[2]

def changeRootValue(root, value):
	root[0] = value

insertLeft(r,3)
insertRight(r,5)
l = getleftChild(r)
insertLeft(l, 7)
print(r)
