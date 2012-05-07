n=2
sum=4
while(n<1001):
    if(n%2==0):
     sum=sum+2*(n*n) +(n+1)+1   
    elif(n%2!=0):
     sum=sum+2*(n*n)+n+1
    n=n+1 
sum=sum+1001*1001
print sum
