a=2
for i in range(1,11):
 print (a,"*",i,"=",a*i)


a=int(input("Enter Number!"))
flag=False
if a==1:
 print(a,"Is not a Prime Number!")
elif a>1:
 for i in range(2,a):
 if(a%i)==0:
 flag=True
 break
 if flag:
 print(a,"Is not a Prime Number!")
 else:
 print(a,"Is a Prime Number!")



n=int (input("Enter The Number!"))
temp=n
rev=0
while n > 0:
 dig=n%10
 rev=(rev*10)+dig
 n=n//10
if(temp==rev):
 print ("Number is Palindrome")
else:
 print ("Number is not a Palindrome")


n=int (input("Terms?"))
n1,n2=0,1;
if n<=0:
 print("Enter Positive Number!")
elif n==1:
 print ("Fibonacci seq Upto",n ,":",n1)
else:
 print ("Fibonacci seq : ",end=" ")
 for n in range(n):
 print(n1,end=" ")
 nth=n1+n2
 n1=n2
 n2=nth
