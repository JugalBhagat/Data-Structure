class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Binary_tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if(self.root is None):
            self.root=Node(data)
        else:
            self.insert_recursive(data,self.root)

    def insert_recursive(self,data,node):
        if(data < node.data):
            if(node.left is None):
                node.left=Node(data)
            else:
                self.insert_recursive(data,node.left)
        else:
            if(node.right is None):
                node.right=Node(data)
            else:
                self.insert_recursive(data,node.right)

    def printt(self):
        if(self.root is None):
            print("Tree is empty")
        else:
            self.print_tree_recursive(self.root,0)
    
    def print_tree_recursive(self, node, depth):
        if node is not None:
            #print("'",node.data,"'",end="")
            self.print_tree_recursive(node.left, depth + 1)
            print("  " * depth + str(node.data))
            self.print_tree_recursive(node.right, depth + 1)
            


T=Binary_tree()
T.insert(5)
T.insert(3)
T.insert(7)
T.insert(1)
T.insert(4)
T.insert(6)
T.insert(8)

T.printt()