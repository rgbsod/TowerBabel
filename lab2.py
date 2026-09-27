from lab1 import Array

class Tower:
	def __init__(self,capacity=10):
		# NOTE: DO NOT EDIT THIS CODE
		# constructor param: array capacity
		# example: stack = ArrayStack(10)
		# set properties: array, size
		self.array = Array(capacity)
		self.size = 0

	def __repr__(self):
		lines = []
		# iterate from top (size-1) down to bottom (0)
		for i in range(self.size - 1, -1, -1):
			lines.append(str(self.array[i]))

		if lines:
			return " \n".join(lines)
		else:
			return "<empty>"


	def is_empty(self):
		# NOTE: DO NOT EDIT THIS CODE
		# check if stack is empty
		return self.size == 0

	def push(self,item):
		if (self.array.capacity <= self.size): #Checks if there is a need to expand the array
			self.array.expand(2*self.array.capacity)
		self.array[self.size] = item
		self.size += 1

	def pop(self):
		if self.is_empty():
			raise Exception('Empty stack: cannot pop')
		else:
			popped = self.array.items[self.size-1]  #assigns "popped" as the current top (latest pushed element) to make it safe to remove
			self.array[self.size-1] = None  #deletes the current top
			self.size -= 1

			return popped
		
	def top(self):
		if self.is_empty():
			#raise Exception('Empty stack: no top')
			return None
		else:
			return self.array[self.size-1]  #returns latest pushed element
		
#Custom Functions for Tower of Hanoi
		
	def check_val_push(self, item):
		target = self.top() #checks if to be pushed item entry is less than current top
		if target.key < item.key:
			return False
		return True

	def move_to(self, tower):
		top_from = self.top()

		if ((tower.top() is None) or (tower.check_val_push(top_from))): #if target tower is empty or condition valid
			tower.push(self.pop())
		else:
			raise Exception('Ring to be pushed is bigger than target tower''s current top!')