from operator import index


#-------------------------------------------- ARRAY ---------------------------------------------------------#
class Array:
	def __init__(self,capacity):
		# NOTE: DO NOT EDIT THIS CODE
		# __init__ method: constructor
		# called when creating new Array objects
		# example: a = Array(10), where capacity = 10
		self.capacity = capacity 
		self.items = []
		for i in range(capacity):		# initialize array with None items
			self.items.append(None)

	def __repr__(self):
		# NOTE: DO NOT EDIT THIS CODE
		# string representation of Array object
		# convert all items to string: 	str(x) for x in self.items
		# use a comma to separate them: ', '.join(...)
		display = ', '.join(str(x) for x in self.items)
		return '[' + display + ']' # wrap with [ ] to look like an array

	def __getitem__(self,index):
		if (0 <= index < self.capacity):
			return self.items[index]
		else:
			raise IndexError("Array.get: Index out of bounds")

	def __setitem__(self,index,item):
		if (0 <= index < self.capacity):
			self.items[index] = item
		else:
			raise IndexError("Array.set: Index out of bounds")
        #removed return


	def expand(self,new_capacity):
		old_array = list(self.items) 
		'''
		makes old_array as a copy of self.items, instead of using for loops to build
		capacity and elements

		used list(self.items) instead of self.items so to ensure old_array is a legit
		copy of og self.items rather than pointing to it, to be safe.
		'''

		self.items = [None] * new_capacity #replaced the for loop. used array reassignment to build new capacity for self.items
		self.capacity = new_capacity
		for i in range(len(old_array)): #now its one loop :]]
			self.items[i] = old_array[i]
        #removed return
		
		
#--------------------------------------------SLL NODE---------------------------------------------------------#
class SLLNode:
	def __init__(self,item=None,next_node=None):
		# NOTE: DO NOT EDIT THIS CODE
		# __init__ method: constructor
		# called when creating new SLLNode objects
		# item and next_node are optional parameters; if not set, use None
		self.item = item 
		self.next = next_node

	def __repr__(self):
		# NOTE: DO NOT EDIT THIS CODE
		# string representation of SLLNode object
		return '<SLLNode: %s>' % str(self.item)

	# Getter and Setter Methods
	# Use self.item and self.next

	def get_item(self):
		return self.item

	def set_item(self,item):
		self.item = item
        #removed return
		
	def get_next(self):
		return self.next

	def set_next(self,next_node):
		self.next = next_node
        #removed return
#--------------------------------------------DLL NODE---------------------------------------------------------#
class DLLNode:
	def __init__(self,item=None,prev_node=None,next_node=None):
		# __init__ method: constructor
		# called when creating new SLLNode objects
		# item, prev_node, next_node are optional parameters; if not set, use None
		self.item = item 
		self.prev = prev_node
		self.next = next_node

	def __repr__(self):
		# string representation of DLLNode object
		return '<DLLNode: %s>' % str(self.item)

	# Getter and Setter Methods
	# Use self.item, self.prev, and self.next

	def get_item(self):
		return self.item

	def set_item(self,item):
		self.item = item
        #removed return
		
	def get_prev(self):
		return self.prev

	def set_prev(self,prev_node):
		self.prev = prev_node
        #removed return

	def get_next(self):
		return self.next

	def set_next(self,next_node):
		self.next = next_node
        #removed return
