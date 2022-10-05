class Node:
	def __init__(self, data:int):
		self.data=data 
		self.right=None
		self.left=None

class Tree:
	def __init__(self, data):
		self.root=Node(data)
	def append(self, data, tree):
		if self.root is None:
			self.root=Node(data)
			return 
		elif self.root.data >= data:
			if self.root.left is None:
				node=Node(data)	
				self.root.left=node
			else:
				self.append(data, self.root.left)	
		elif self.root.data < data:
			if self.root.right is None:
				node=Node(data)	
				self.root.right=node
			else:
				self.append(data, self.root.right)
	def printT(self, tree):
		if tree is None:
			return 
		print(tree.root.data)
		self.printT(tree.root.left)
		self.printT(tree.root.right)

tree1=Tree(15)

tree1.append(5, tree1)
tree1.append(4, tree1)
tree1.append(6, tree1)
#tree1.printT(tree1)