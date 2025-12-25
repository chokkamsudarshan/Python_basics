# swapping of two numbers without third number
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
#swapping
# it will wrkk only for integer values not for str or float
a=a^b
b=a^b
a=b^a
print("swapped value of a is {},swapped value of b is {}".format(a,b))