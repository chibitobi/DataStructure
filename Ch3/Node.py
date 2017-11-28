class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self, newdata):
		self.data = newdata
	def setNext(self,newnext):
		self.next = newnext


class UnorderedList:
	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None
	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found =True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
	def append(self,item):
		current = self.head
		if current:
			while current.getNext() != None:
				current = current.getNext()
			current.setNext(Node(item))
		else:
			self.head = Node(item)
	
	def returnResults(self):
		current = self.head
		while current:
			print(current.getData())
			current = current.getNext()

#temp = Node(93)
#print(temp.getData())

mylist = UnorderedList()
mylist.add(41)
mylist.add(17)
mylist.append(55)
print(mylist.returnResults())
