# Assigment operator
# = Simple Assignment operator
# shift value from right to left variable
from array import array
from unicodedata import name


var1 = 20 # 20 assigned to var1
print(var1)

var1, var2 = 34, 35
print(var1, var2)

var1, var2 = var2, var1 #swap
print(var1, var2)
#Multiple Assignment
var1 = var2 = var3 = 100
print(var1, var2, var3)
print(id(var1))
print(id(var2))
print(id(var3))


#Short-Hand Assignment Operator
num1 = 20
print(id(num1))
# num1 = num1 + 5
num1+=5
print(id(num1))
print(num1)
#2. Arithmetic Operators
import math
var1 = 20
var2 = 70
var3 = var1 // var2
var4 = var1%var2
var5 = var1** var2
print(var3, var4, var5)
var6 = math.pow(2,4)
var7 = math.sqrt(49)
print(var7)
#relational operators
#compare two values and return boolean result
# ==Equals to
#value1 is equals to value2 -> True
var1 = {1,2,3}
var2 = {4,5,6}
result = (var1 == var2) 
print(result)
#Greater than >
#left value is greater than right value
v1 = 12
v2 = 20
result = v1 <  v2
print(result)

#greater than or equals to
#left value is greater than or queals to right value -> True
v1 =10
v2 = 5
result =v1>=v2
print(result)
#less than or equals to
#left value is less than or equals to right value -> True
v1 = 10
v2 = 10
result =v1<=v2
print(result)       
#Not equals to ! =
#left value is not equals to right value
v1= 20
v2 = 20
result1 = v1==v2
result2 = v1!=v2
print(result1,result2)
#logical operator
#a. and
result = (10>5) or (10>6)
print(result)
result = (10>50) or (10>6)
print(result)
#b.or
#c. not
#True->False
#False->True
print(not True)
print(not False)
print(not True or True)
print(not False and False)
#other operators
#[], {}, ()
#Result Processing
#declare
sid=None
Fullname= None
sub1=None #obtained mark
sub2 =None
sub3 =None
sub4 =None
#input
sid = input("Enter student ID: ")
sub1= input("Enter first subject: ")
sub2 = input("Enter second subject: ")
sub3 = input("Enter third subject: ")
sub4 = input("Enter fourth subject: ")
#process
#output
print("SID : {}".format(sid))
print("sub1 : {}".format(sub1))
print("sub2 : {}".format(sub2))
print("sub3 : {}".format(sub3))
print("sub4 : {}".format(sub4))
Total = sub1+sub2+sub3+sub4
average = (Total/4)

