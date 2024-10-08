#!/bin/env python3

# Method is a block of code with a name that we can call and reuse  
# Method can be procedure or function

# Procedure:
# Procedure is a method that does an action
# Procedure then is a verb
# Procedure does not return a value
# Syntax: 
# def <verb> (args):
#   <code - action>


# Function:
# Function is a method that returns a value
# Function is a noun
# Function can be stored in a variable
# Syntax:
# def <noun>(args):
#   <code>
#   return <value(s)>


# Requirements:
# 1- Read a positive integer n from STDIN
# 2- Calculate the factorial of n
# 3- Calculate the: perimeter, area, volume, (circle/sphere of radius n)
# 4- Show the collatz table of n
import math as m 
n = int(input('n = '))

def factorial(n):
    f = 1
    for e in range(2,n+1):
        f *= e   
    return f

var = factorial(n)
print(f'Factorial({n}) = {var}')


def geometry(n):
    p = 2*m.pi*n  
    a = m.pi*pow(n,2)
    v = (4/3)*m.pi*m.pow(n,3)
    return p, a, v

p, a, v = geometry(n)
print(f'Perimeter = {p:.2f} - Area = {a:.3f} - Volume = {v:.4f}')

def show_collatz(n):
    while n > 1:
        if n%2 == 0:
            print(f'{n:4} - {int(n/2):4}')   
            n = int(n/2)   
        else:
            print(f'{n:4} - {3*n+1:4}')
            n = 3*n + 1
show_collatz(n)




















