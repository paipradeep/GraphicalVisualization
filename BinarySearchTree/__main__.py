from __future__ import print_function
import sys
from graphviz import Digraph
from Treeclass import BST

#dictionary = {1:insert,2:inorder,3:preorder,4:postorder,5:height}
d = Digraph(comment="graphviz file",format="png")
tree = BST()
z = 0
#fp = open("image.gv","w+")
while True:
	choice = int(raw_input("Enter Choice:\n\t1-Insert Node\n\t2-Inorder\n\t3-Preorder\n\t4-Post order\n\t5- find height\n\t6-Draw tree"))
	#if choice in dictionary:
	if(choice == 1):
		data = int(raw_input("\nEnter data to be inserted"))
		newNode = tree.createNode(data)
		tree.root = tree.insert(newNode,tree.root)
	elif(choice == 2):
		tree.inorder(tree.root)
	elif(choice == 3):
		tree.preorder(tree.root)
	elif(choice == 4):
		tree.postorder(tree.root)
	elif(choice == 5):
		print("Height:",tree.height(tree.root))
	elif(choice == 6):
		#fp.write("digraph {")
		if tree.root!=None:
			d.name = "Binary_Search_Tree"
			d.filename = "RenderedBST.gv"
			d.node(str(tree.root.data))
			tree.drawBST(tree.root,d)
			d.render()
			print("\n\n Tree drawn Successfully")
			sys.exit()
		else:
			print("Tree is empty.")
	else:
		sys.exit()
		
