from NodeClass import Node
class Tree:
    def __init__(self):
        self.root = None

    def balanceFactor(self,root):
        if root == None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def leftRotate(self,root):
        temp = root
        root = root.right
        temp.right = root.left
        root.left = temp
        return root

    def rightRotate(self,root):
        temp = root
        root = root.left
        temp.left = root.right
        root.right = temp
        return root

    def normalInsert(self,root,newNode):
        if(root == None):
            return newNode
        if(newNode.data<root.data):
            root.left = self.normalInsert(root.left,newNode)
        else:
            root.right = self.normalInsert(root.right,newNode)
        return root

    def insert(self,root,newNode):
        if root == None:
            return newNode
        if newNode.data < root.data:
            root.left = self.insert(root.left,newNode)
        else:
            root.right = self.insert(root.right,newNode)
        if (self.balanceFactor(root) > 1):
            if(newNode.data < root.left.data):
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root.right)
        elif(self.balanceFactor(root) < -1):
            if(newNode.data > root.right.data):
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def max(a,b):
        if a>b:
            return a
        return b
    def inorder(self,root):
        if(root == None):
            return
        self.inorder(root.left)
        print root.data
        self.inorder(root.right)

    def height(self,root):
        if(root == None):
            return 0
        return 1+max(self.height(root.left),self.height(root.right))

    def drawTree(self,root,d,z):
        if root == None:
            return
        #global z
        if(root.left == None):
            z +=1
            d.node("Leaf"+str(z),shape="point")
            d.edge(str(root.data),"Leaf"+str(z),color="red")
        else:
            d.edge(str(root.data),str(root.left.data),color="blue")
        if(root.right == None):
            z+=1
            d.node("Leaf"+str(z),shape="point")
            d.edge(str(root.data),"Leaf"+str(z),color="red")
        else:
            d.edge(str(root.data),str(root.right.data),color="blue")
        self.drawTree(root.left,d,z)
        self.drawTree(root.right,d,z+10)
