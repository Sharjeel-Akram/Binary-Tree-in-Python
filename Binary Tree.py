class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None    
class Binary_Tree:
    def __init__(self):
        self.root = None
        self.flag = False
    def getroot(self):
        return self.root
    def insert_Node(self,node):
        if (self.root is None):
            self.root = node
        else:
            temp = [self.root]
            for current in temp:
                if current.left != None and current.right != None:
                    temp.append(current.left)
                    temp.append(current.right)
                else:
                    if current.left == None:
                        current.left = node
                        return
                    elif current.right == None:
                        current.right = node
                        return
    def search_Node(self, Current, value):   
        if(self.root == None):  
            print("Tree is empty") 
        else:   
            if(Current.data == value):  
                self.flag = True  
                return
            if(self.flag == False and Current.left != None):
                self.search_Node(Current.left, value)
            if(self.flag == False and Current.right != None):
                self.search_Node(Current.right, value)
    def Height(self):
        if self.root == None:
            print("root is empty")
        current = self.root
        count = 0
        while current.left != None:
            current = current.left
            count = count + 1
        return count 
    def In_Order(self,node):
        if node != None:
            self.In_Order(node.left)
            print(node.data)
            self.In_Order(node.right)   
    def Pre_Order(self,node):
        if node != None:
            print(node.data)
            self.Pre_Order(node.left)
            self.Pre_Order(node.right)
    def Post_Order(self,node):
        if node != None:
            self.Post_Order(node.left)
            self.Post_Order(node.right)
            print(node.data)
root = Binary_Tree()
root.insert_Node(Node(20))
root.insert_Node(Node(36))
root.insert_Node(Node(10))
root.insert_Node(Node(35))
root.insert_Node(Node(69))
root.insert_Node(Node(25))
root.insert_Node(Node(16))
root.insert_Node(Node(19))
root.insert_Node(Node(98))
root.insert_Node(Node(56))
choice = input("pleased enter your choice from a,b,c,d,e,f,g: ")
if choice == "a":
    loop = input("enter how many time you want to insert node: ")
    for i in range(int(loop)):
        N = int(input("please enter the value for node: "))
        root.insert_Node(Node(N))
    print("In_Order Values")
    root.In_Order(root.getroot())
    print("Pre_Order Values")
    root.Pre_Order(root.getroot())
    print("Post_Order Values")
    root.Post_Order(root.getroot())
if choice == "b":
    Node = int(input("enter the node which you want to seach in tree: "))
    root.search_Node(root.root,Node)  
    if(root.flag):  
        print("Node exists in the binary tree")  
    else:  
        print("Node does not exist in the binary tree") 
if choice == "c":
    print(root.Height())
if choice == "d":
    print("Pre_Order Values")
    root.Pre_Order(root.getroot())
if choice == "e":
    print("In_Order Values")
    root.In_Order(root.getroot())
if choice == "f":
    print("Post_Order Values")
    root.Post_Order(root.getroot())   
if choice == "g":
    print("Program has been ended.")