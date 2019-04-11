"""
a="abc"
b=1

x=str(input("input value of x"))
#it converts the variable into structure so it not add it connect to each other.
y=str(input("input value of y"))
z=x+y
print(z)


a=input("input value of a")
b=input("input value of b")
c=a+b
print(c)


name=raw_input("your name plz ")#in python3 we write only input
print("Hello, "+name)#everything is in string

#import file
import sys
print(len(sys.argv))#shows the length 
print(sys.argv)#shows the file content??????????????


print (1/2)#int value
print(1/2.0)#float value
print(float(1)/2)#float value
print(1/float(2))#float value

"""
a="hello"
b=a*3
print a
print (b )


print(abs(-4))#4
print(abs(4))#4


print(cmp(1,-4))#1
print(cmp(1,1))#0
print(cmp(1,4))#-1"""


import math
print(math.ceil(1.254))#2.0
print(math.floor(1.254))#1.0
print(math.exp(1))#f(x)=e^x#2.7182
print(math.exp(5))#148.4131
print(math.log(1.3453))#0.2966
print(math.log10(1.3453))#0.1288
print(max(1,5,6,9,8))
print(min(1,5,6,9,8))
print(math.modf(-5.236548))#(-0.23654799999999998, -5.0)
print(math.modf(5.236548))#(0.23654799999999998, 5.0)
print(pow(2,3))#2^3#always int#8
print(math.pow(2,3))#always float#8.0
print(2**3)#int#8
print(round(1.456789))#1.0
print(round(1.556789))#2.0
print(round(1.456789,3))#1.457
print(math.sqrt(4))#2.0

