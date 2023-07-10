#make a node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self,data):
        newnode=Node(data)   
        if(self.head==None):
            self.head=newnode
            newnode.next=self.head
            #print(newnode.data)
        else:
            cur_node=self.head
            while cur_node.next != self.head:
                cur_node=cur_node.next
            cur_node.next=newnode
            newnode.next=self.head
            #print(newnode.data)

    def printt(self):
        if(self.head is None):
            print("Empty")
        cur_node=self.head
        while cur_node.next != self.head:
            print(cur_node.data)
            cur_node=cur_node.next
        print(cur_node.data)


    def delete(self,data):
        cur_node=self.head
        while True:
            if(cur_node.data is data):
                prev.next=cur_node.next
                #print(cur_node.data)
                break
            prev=cur_node
            cur_node=cur_node.next
        


f=Node("jack")
ll=linklist()
ll.insert_at_end("1")
ll.insert_at_end("4")
ll.insert_at_end("2")
ll.insert_at_end("3")

ll.delete("3")

ll.printt()