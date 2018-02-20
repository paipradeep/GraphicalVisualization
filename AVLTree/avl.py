import sys
from graphviz import Digraph
from NodeClass import Node
from TreeClass import Tree

avl = Digraph(comment="AVL tree",format="png")
binary = Digraph(comment="Binary tree",format="png")
myTree = Tree()
dummy = Tree()
print "1-Insert\t2-inorder\t3-height\t4-draw tree"
#insertionOrder = []
while(1):

    ch = int(raw_input("Enter choice:"))
    if(ch == 1):
        data = int(raw_input("Enter new node data"))
        #insertionOrder.append(data)
        myTree.root = myTree.insert(myTree.root,Node(data))
        dummy.root = dummy.normalInsert(dummy.root,Node(data))
    elif ch == 2:
        myTree.inorder(myTree.root)
    elif ch == 3:
        print myTree.height(myTree.root)
    elif ch == 4:
        if myTree.root == None:
            print "Tree is empty"
        else:
            z = 0
            avl.name = "AVL_Tree"
            avl.filename = "avlTree.gv"
            avl.node(str(myTree.root.data))
            myTree.drawTree(myTree.root,avl,z)
            avl.render()
            z = 0
            binary.name = "Unbalanced_Tree"
            binary.filename = "unbalanced.gv"
            binary.node(str(dummy.root.data))
            dummy.drawTree(dummy.root,binary,z)
            binary.render()

    else:
        sys.exit()
