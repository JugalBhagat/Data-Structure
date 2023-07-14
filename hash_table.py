class hashtable:
    def __init__(self,n):
        self.size=n
        self.table= [[] for _ in range(n)]

    def hash_val(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        inx=self.hash_val(key)
        for ht in self.table[inx]:
            if(key==ht[0]):
                ht[1]=value 
                return
        self.table[inx].append([key,value])

    def get(self,key):
        inx=self.hash_val(key)
        for ht in self.table[inx]:
            if(ht[0]==key):
                return ht[1]
        return "not found"
    
    def remove(self, key):           # chatgpt
        index = self.hash_val(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        return "Key not found"

    def remove2(self,key):             # mine
        index=self.hash_val(key)
        for ht in self.table[index]:
            if(ht[0]==key):
                self.table[index].clear()

ht=hashtable(10)
ht.insert("apple","6")
ht.insert("orange","7")
ht.insert("banana","8")
ht.insert("mango","9")

ht.get("apple")

print(ht.table)

ht.remove("apple")
ht.remove2("banana")

print(ht.table)