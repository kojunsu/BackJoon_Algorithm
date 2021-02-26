num1=input()
num1=int(num1)
n=num1
sum=0

while(1):
    a=n%10
    b=n//10
    n=10*a+(b+a)%10
    
    sum+=1
    if(n==num1):
        break
print(sum)