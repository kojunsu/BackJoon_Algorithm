n=int(input())
star="*"
blank=" "
for i in range(1,n+1):
  print("%s"%(blank*(n-i)),end="")
  print("%s"%(star*i))

  