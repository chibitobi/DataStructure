a=5
b=6
#These are considered constant time
'''
for i in range(n):
	for j in range(n):
		x = i * i
		y = i * j
		z = i * j
		#This entire loop is considered 3n^2 time
		#as there are three equations who are doing n^2 time operations
	
for k in range(n):
	w = a*k + 45
	v = b*b
	#this is 2n time
d = 33	
'''

arraylist = [6, 2, 3, 4, 8, 2]
def minfunction(alist):
	minimum = alist[0] #initial guess
	for i in alist:
		smallest = True
		for j in alist:
			if i > j:
				smallest = False
		if smallest == True:
			minimum = i
	return minimum						
#This is n^2 time


def minlinearfunct(alist):
	minimum = alist[0]
	for i in alist:
		if i < minimum:
			minimum = i
	return minimum
#this is linear time

def kthsmallest(alist, k):
	current = alist[0]
	placement = 1
	for i in alist:
		if current < i:
			current = i
		elif current > i:
			placement += 1
			target = current
			print(placement, k, target)
		if (k == placement):
			print("Im here")
			return target

print(arraylist)
print(minfunction(arraylist))
print(minlinearfunct(arraylist))
print(kthsmallest(arraylist,5))
