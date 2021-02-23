n=int(input())
A=[]
B=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    A.append(a)
    B.append(b)
    
for j in range(n):
    print(A[j]+B[j])