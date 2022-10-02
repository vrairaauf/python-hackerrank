class Node:
	def __init__(self, value:int):
		self.__value=value
		self.__Next=None
	def getValue(self):
		return self.__value
	def getNext(self):
		return self.__Next
	def setNext(self, node):
		self.__Next=node


class LinkedList:
	def __init__(self):
		self.Head=None
	##############################
	def append(self, value:int):
		node=Node(value)
		if self.Head is None:
			self.Head=node
			return 
		else:
			vHead=self.getHead()
			while vHead.getNext() is not None:
				vHead=vHead.getNext()
			vHead.setNext(node)
	##############################
	def appendMany(self, *args):
		for arg in args:
			self.append(arg)
	##############################
	def preAppend(self, value):
		node=Node(value)
		if self.Head is None:
			self.Head=node
			return
		node.setNext(self.Head)
		self.Head=node
	##############################
	def preAppendMany(self, *args):
		for arg in args:
			self.preAppend(arg)
	################################
	def show(self):
		vHead=self.getHead()
		while vHead.getNext() is not None:
			print(vHead.getValue())
			vHead=vHead.getNext()
		print(vHead.getValue())
	##############################
	def getHead(self):
		return self.Head;
ls=LinkedList()

ls.append(7)
ls.append(7)
ls.append(7)
ls.appendMany(5,4,10,89)
ls.preAppend(102)
ls.show()

def hiArgs(*args):
	for arg in args:
		print(arg)
#hiArgs(1, 2, 3, 85, 41)