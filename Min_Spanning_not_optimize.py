import sys
class graph:
    
    def __init__(self,vertx):
        self.V=vertx
        self.G=[[0 for i in range(vertx)]  for j in range(vertx)]
       

    def primMST(self,gr,tempD1,tempD2,tempA,un,R):
        gr=gr
        tempD1=tempD1
        tempD2=tempD2
        tempA=tempA
        un=un
        R=R
        minn=999999999
        J=0
        I=0
        for i in un:
            for j in range(self.V):
                if(gr[i][j] < minn and gr[i][j]!=0):
                    minn=gr[i][j]
                    J=j
                    I=i
        if(minn==gr[I][J]):
            un.append(J)
            gr[I][J]=gr[J][I]=0
            tempD1.append(I)
            tempD2.append(J)
            tempA.append(minn)
            R[J]=True
            minn=999999999
        if(len(un)!=5):
            self.primMST(gr,tempD1,tempD2,tempA,un,R)

        for i in range(4 ):
            print(tempD1[i],"-",tempD2[i],"=",tempA[i]) 
        print("hello")
        sys.exit()
            #temp.append(minn)
            #minn=min(temp)
            #inx=temp.index(minn)
            #R[inx]="True"
            #un.append(inx)

N=5
g=graph(N)
g.G=[
    [0, 7, 0, 6, 0],
    [7, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
g.primMST(g.G,[],[],[],[0],[False for i in range(N)])
