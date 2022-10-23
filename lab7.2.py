class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def height(root): 
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0 
    # Recursively call height of each node
    else:
        leftAns = height(root.left)
        rightAns = height(root.right)
 
        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1
 
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
    
        else:
            currentNode = self.root
            while True:
                if data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    else:
                        currentNode = currentNode.right                    
                elif data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    else:
                        currentNode = currentNode.left
        return self.root

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is : " + str(height(root)-1))
