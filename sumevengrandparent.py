class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    
       
    #how to check granparent
def sumEvenGrandparent(self, root: Node) -> int:
    def findParent(root, val, parent):
        if (root == None): 
            return; 
        if (root.data == val):
            print(parent)
        else:
            findParent(root.left, val, root.data) 
            findParent(root.right, val, root.data)
        

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()