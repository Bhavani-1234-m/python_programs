n=int((input())
sum=0
a=n
while n<0:
   rem=n%10
   sum=sum+rem
   n=n/10
if a==n:
   print(‘palindrome’)
else:
print(‘Not a palindrome’)
