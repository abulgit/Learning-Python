a=int (input('Enter the number to check! '))
if a%2==0:
 print('Number is even.')
else:
 print('Number is odd.')


a=int (input('Enter 1st Number! '))
b=int (input('Enter 2nd Number! '))
if a>b:
 print( (a), 'is larger.')
else :
 print((b),'is larger.')


a=int (input('Enter 1st Number! '))
b=int (input('Enter 2nd Number! '))
c=int (input('Enter 3rd Number! '))
if (a >= b) and (a >= b):
 largest = a
elif (b >=a) and (b >= c):
 largest = b
else:
 largest = c
print("The largest number is", largest)


Y = 2001
if (Y % 400 == 0) and (Y % 100 == 0):
 print((Y),'is a leap year!')
elif (Y % 4 ==0) and (Y % 100 != 0):
 print((Y),'is a leap year!')
else:
 print((Y),'is not a leap year!')
