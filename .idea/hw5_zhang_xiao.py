import random
import sys

# Cellular Automata

# Define function to check if a belongs to list b
def notin(a,b):
    for i in range(len(b)):
        if a == b[i]:
            return False
    return True

# put an element into a list if this element does not belong to the list
def putin(b,a):
    if notin(a,b):
        b.append(a)
    

def CA():
    # Set Arbitrary Initial Configuration
    ''' I build up the ghost boundary around the configuration matrix,
        such that each element has four neighbors '''
    ghost=[]
    for i in range(N+2):
        ghost.insert(0,0)
    C0=[ghost,ghost]
    for i in range(M):
            k=[0,0]
            for j in range(N):
                r=random.random()
                if r < 0.7:
                    k.insert(j+1,0)  # healthy
                else:
                    k.insert(j+1,1)  # sick
            C0.insert(i+1,k)
    # printing the initial configuration
    print 'Initial Configuration ='
    for i in range(M):
        print C0[i+1][1:N+1]
    change=1
    step=0
    C1=C0
    bdry=[]
    checknew=[]
    for i in range(M):
        for j in range(N):
            if C0[i+1][j+1] == 1:
                checknew.append([i+1,j+1])
                
    while change > 0:
        change=0
        step=step+1
        for i in checknew:
            p=i[0]
            q=i[1]
            if C0[p-1][q] == 0:   # neighbor above
                putin(bdry,[p-1,q])
            if C0[p][q+1] == 0:   # neighbor right
                putin(bdry,[p,q+1])
            if C0[p+1][q] == 0:   # neighbor below
                putin(bdry,[p+1,q])
            if C0[p][q-1] == 0:   # neighbor left
                putin(bdry,[p,q-1])
        checknew=[]
        for j in bdry:
            s=j[0]
            t=j[1]
            if (0<s<M+1) and (0<t<N+1):
                if C0[s-1][t]+C0[s][t+1]+C0[s+1][t]+C0[s][t-1] >= 2:
                    C1[s][t] = 1
                    change=change+1
                    checknew.append([s,t])
                    bdry.remove([s,t])
        C0=C1
                
    print 'Final Configuration = '
    for i in range(M):
        print C0[i+1][1:N+1]
    print 'Step(s) = ', step

sys.stdout=open('hw5_zhang_xiao.txt',"w")
M=20
N=20
CA()
sys.stdout.close() 
