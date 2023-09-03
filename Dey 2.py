str = input ('Enter any String!\n')
print (str.upper())


str = input ('Enter any String!\n')
print (str.lower())


str = input ('Enter any String!\n')
print (str.replace('i','.'))


cel =float(input('Enter Temp. In Celscius\n'))
fahrenheit = (cel * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(cel,fahrenheit)



m=float(input('Enter The Mass of The object!:-'))
v=float(input('Enter The velocity of The object!:-'))
h=float(input('Enter The Hight of The object!:-'))
g=10 #given
KE=0.5 *m*(v*v)
PE=m*g*h
print ('Kinetic Energy of The Object is', KE)
print ('Potential Energy of The Object is', PE)




x=input('Enter The 1st Fraction in / format: ')
y=input('Enter The 1st Fraction in / format: ')
p,q=x.split("/")
r,s=y.split("/")
a=int(p)
b=int(q)
c=int(r)
d=int(s)
m=(a*d)+(b*c)
n=b*d
final="/".join([str(m),str(n)])
print(final)
