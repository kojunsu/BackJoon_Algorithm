A=[]
B=[]
a=1
b=1
while(a+b!=0):
    a,b =list(map(int,input().split()))
    A.append(a)
    B.append(b)
sum=0
while(A[sum]+B[sum]!=0):
    print(A[sum]+B[sum])
    sum+=1

