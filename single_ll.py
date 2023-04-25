#make a node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
    
    def insert(self,newnode):
        if(self.head==None):
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def printt(self):
        if(self.head is None):
            print("Empty")
        cur_node=self.head
        while True:
            if(cur_node is None):
                break;
            print(cur_node.data)
            cur_node=cur_node.next

    def delete(self,node):
        cur_node=self.head
        while True:
            if(cur_node is None):
                print("Not found ",node)
                break
            elif(cur_node.data == node):
                print(node," deleted")
                break
            prev=cur_node
            cur_node=cur_node.next

        if(cur_node is None):
            return
        
        prev.next=cur_node.next
        cur_node.data=None
        


f=Node("jack")
ll=linklist()

ll.insert(f)
s=Node("jason")
ll.insert(s)
t=Node("Jugal")
ll.insert(t)

ll.printt()
ll.delete("Jugal")

ll.printt()