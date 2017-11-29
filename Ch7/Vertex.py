class Test:
	def __repr__(self):
		return "test()"
	def __str__(self):
		return "member of test"

t = Test()
print(repr(t))



class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight
	#def __str__(self):
	#str() built-in function used for class, computing the "informal" string
	#representation of an object
