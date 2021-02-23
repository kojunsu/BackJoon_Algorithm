import sys
n=int(input())
A=[]
B=[]
for i in range(n):
    a,b=list(map(int,sys.stdin.readline().split()))
    A.append(a)
    B.append(b)
    
for j in range(n):
    print(A[j]+B[j])
    