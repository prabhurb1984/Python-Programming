#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import cmath
a=float(input("enter A:"))
b=float(input("enter B"))
c=float(input("enter C"))

d=(b**2)-(4*a*c)

sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("the solutions are {0} and {1}".format(sol1,sol2))