n=int(input())

for i in range(1,n+1):
  a,b=list(map(int,input().split()))
  sum=a+b
  print("Case #%d: %d + %d = %d" %(i,a,b,sum))
  