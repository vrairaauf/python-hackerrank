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
		self.size=0;
	#############################
	def getSize(self):
		return self.size
	##############################
	def append(self, value:int):
		node=Node(value)
		if self.Head is None:
			self.Head=node
		else:
			vHead=self.getHead()
			while vHead.getNext() is not None:
				vHead=vHead.getNext()
			vHead.setNext(node)
		self.size=self.size+1
	##############################
	def appendMany(self, *args):
		for arg in args:
			self.append(arg)
	##############################
	def preAppend(self, value):
		node=Node(value)
		if self.Head is None:
			self.Head=node
			self.size=self.size+1
			return
		node.setNext(self.Head)
		self.Head=node
		self.size=self.size+1
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
	##############################
	def delete(self):
		if self.Head is None:
			print("empty linked list !!")
			return 
		if self.Head.getNext() is None:
			self.Head=None
			self.size=self.size-1
			return
		vHead=self.getHead()
		while vHead.getNext().getNext() is not None:
			vHead=vHead.getNext()
		vHead.setNext(None)
	############################### 
	def debDelete(self):
		self.Head=self.getHead().getNext()
		self.size=self.size-1
	############################### 
	def compare(self, list1)->bool:
		if(self.getHead() is None and list1.getHead() is None):
			return True;
		if(self.getSize() != list1.getSize()):
			return False;
		vHead1=self.getHead()
		vHead2=list1.getHead()
		while vHead1 is not None and vHead2 is not None:
			if vHead1.getValue()==vHead2.getValue():
				vHead1=vHead1.getNext()
				vHead2=vHead2.getNext()
			else:
				return False
		return True
	############################
ls=LinkedList()
ls2=LinkedList()
ls.append(7)
ls.append(7)
ls.append(7)
ls.appendMany(5,4,10,89)
ls.preAppend(102)
ls.delete()
ls.delete()
ls.debDelete()

ls2=LinkedList()
ls2.append(7)
ls2.append(7)
ls2.append(7)
ls2.appendMany(5,4,10,89)
ls2.preAppend(102)
ls2.delete()
ls2.delete()
ls2.debDelete()

if ls.compare(ls2):
	print("equals lists")
