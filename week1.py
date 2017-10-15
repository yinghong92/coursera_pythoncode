#def add(x,y) : return x+y
# add=lambda x,y: x+y
# print add(3,5)

# Fibonacci
# def fib(n):
#     a, b = 0, 1
#     count=1
#     while count < n:
#         a,b=b, a+b
#         count =count+1
#     print a
#
# def fib(n):
#   if n==0 or n==1:
#         return n
#     else:
#         return (fib(n-1)+fib(n-2))
# # # #
# def hanoi(a,b,c,n):
#     if n==1:
#         print a, '->', c
#     else:
#         hanoi(a,c,b,n-1)
#         print a,'->', c
#         hanoi(b,a, c,n-1)
# hanoi('a','b', 'c', 4)

import math
# num=-1234
# def fun(num):
#     if num<0:
#         print '-',
#         num = -num
#     if num/10:
#         fun(num/10)
#     print chr(num%10+48),
# print fun(num)

# def proc(n ):
#     if (n<0):
#         print '-',
#         n = -n
#     if (n / 10):
#         proc(n / 10 )
#     print n % 10,
#
# proc(-345 )
# "a" is "a"
# x = "a"
# "aa" is "a"*2
# print x * 2
# print "aa"
# print type("aa")
# print type("x")
# def test(x):
#     if isinstance(x, list):
#         x.append(4)
#         print x
#     elif isinstance(x, int):
#         x += 1
#         print x
# array = [1, 2, 3]
#
# test(array)
# def my_power(x, n = 2):
#     s = 1
#     while n > 0:
#         n -= 1
#         s = s * x
#     return s
# print my_power(3, 3)
from math import sqrt
def isprime(x):
     if x == 1:
         return False
     k = int(sqrt(x))
     for j in range(2,k+1):
           if x%j == 0:
                 return False
     return True
if __name__ == "__main__":
    flag = 'y'
    while(flag == 'y'):
        num = input("Please input a number:")
        for i in range(2,num):
            if isprime(i) and i<int(sqrt(num)) and num % i ==0:
                print i,
        flag = raw_input("\nIf you want to input another number,input y please or input n.")
