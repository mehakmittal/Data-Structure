class Node(object):

	def __init__(self, data=None):
		self.right = None
		self.data = data


class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, data):
		newNode = Node(data)
		if self.first is None and self.last is None:
			self.first = newNode
			self.last = self.first
		else:
			self.last.right = newNode
			self.last = newNode

	def dequeue(self):
		if self.first is None:
			return None
		else:
			data = self.first.data
			next = self.first.right
			if next is None:
				self.first = None
				self.last = None
			else:
				self.first = next
			return data
