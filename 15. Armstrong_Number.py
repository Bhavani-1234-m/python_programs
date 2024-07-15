n=int(input(‘enter the number’)
sum=0
rem=0
a=n
while n!=0:
rem=n%10
sum=sum+rem*rem*rem
n=n/10
if(a==n):
   print(‘armstrong’)
else:
print(‘Not an armstrong’)
