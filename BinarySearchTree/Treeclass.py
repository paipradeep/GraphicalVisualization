from Nodeclass import Node

class BST:
	#root = None
	z = 0
	count = 0
	def __init__(self):
		self.root = None
		
	def createNode(self,data):
		newNode = Node(data)
		return newNode
	
	def insert(self,newNode,currentNode):
		if currentNode == None:
			currentNode=newNode
		elif newNode.data <= currentNode.data:
			currentNode.left=self.insert(newNode,currentNode.left)
		else:
			currentNode.right=self.insert(newNode,currentNode.right)
		self.count += 1
		return currentNode
			
	
		
	def drawBST(self,root,d):
		#global z
		#global d
		if root == None:
			return
		if root.left == None:
			self.z+=1
			d.node("leaf"+str(self.z),shape="point")
			d.edge(str(root.data),"leaf"+str(self.z),color="red")
			
		else:
			d.edge(str(root.data),str(root.left.data),color="blue")
		if root.right == None:
			self.z +=1
			d.node("leaf"+str(self.z),shape="point")
			d.edge(str(root.data),"leaf"+str(self.z),color="red")
		else:
			d.edge(str(root.data),str(root.right.data),color="blue")
		self.drawBST(root.left,d)
		self.drawBST(root.right,d)
		
	
	def inorder(self,root):
		if root == None:
			return
		self.inorder(root.left)
		print(root.data)
		self.inorder(root.right)
	
	def preorder(self,root):
		if root == None:
			return
		print(root.data)
		self.preorder(root.left)
		self.preorder(root.right)
	
	def postorder(self,root):
		if root == None:
			return
		self.postorder(root.left)
		self.postorder(root.right)
		print(root.data)
		
	def height(self,root):
		if root == None:
			return -1
		return 1+max(self.height(root.left),self.height(root.right))
	
			
		



		
	

			
		
