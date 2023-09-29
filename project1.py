# Project1
# Deadline - September 1, 23. Upload your solution to the dropbox in iLearn.

# Part1. (50%) Exercise 1.1: 11a /page 8

# Part2. (50%) Implement Consecutive integer checking algorithm for computing gcd(m, n).

# Part3. (30%) (BONUS) Implement Middle-school procedure for computing gcd(m, n).

# 	The goal of this programming assignment is to implement a function that calculates the Greatest Common Divisor (GCD) of two integers, and then output the result along with the provided input values. You will be required to create a command-line program that takes two integer arguments, m and n, calculates their GCD, and displays the result in the format: gcd(m, n) = v, where m and n are the input values, and v is the calculated GCD, or "undefined" if no GCD exists.

# 	You have the flexibility to implement each algorithm using the programming language of your choice.

# 	Your project implementations must meet the following requirements:
# - Compile without any warnings.
# - Include proper documentation.

import sys

################################################################################# EXTENDED EUCLIDS ALGORITHM

def extEuclid (a,b): 
   # returns a triple (d,s,t) such that d = gcd(a,b) and
   # d == a*s + b*t

   a = float(a)
   b = float(b)

   if a == 0 and b == 0:
    return ("Undefined","Undefined","Undefined")

   if b == 0: 
      return (a,1,0) 
   
   (d1, s1, t1) = extEuclid(b,a%b) 
   d = d1 
   s = t1 
   t = s1 - (a // b) * t1 ;   # note: div = integer division
   return (abs(d),s,t) 

#################################################################### CONSECUTIVE INTEGER CHECKING ALGORITHM


#consecutive integer checking algorithm decrements from the minimum number of m and n until it reaches the gcd
def CICA(m,n):  
    m = abs(float(m))
    n = abs(float(n))
    t = min(m,n)

    if m == 0 and n == 0:
        return "Undefined"
    if m == 0:
        return n
    while(t > 0):
        if m % t == 0: # checks to see if both m or n will divide properly, if not then it will decrement until it finds the GCD
            if n % t == 0:
                return t
        t-=1

################################################################################# MIDDLE SCHOOL PROCEDURE
def factor(num): # factors a single number out into an array
    num = abs(num)
    factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor+=1

    return factors


# puts similar factors from two arrays into a single one
def factorComparison(a,b): 
    factors = []
    for i in a:
        if i in b:
            factors.append(i)
            b.remove(i)
            
    return factors


# multiplies up all of the similar factors in both numbers
def middleSchoolProcedure(a,b): 
    a = abs(float(a))
    b = abs(float(b))
    total = 1

    if a == 0 and b == 0:
        return "Undefined"
    if a == 0:
        return b

    for i in factorComparison(factor(a),factor(b)):
        total*=i
    return total

#############################################################################################################
      
m = sys.argv[1] #argument 1
n = sys.argv[2] #argument 2

stuff = extEuclid(m,n) # putting all information into variable "stuff" for ease of use

print("Extended Euclids Algorithm: gcd(",m,",",n,") = ")
print("\tGCD / V : ",stuff[0])
print("\tCoefficient 1:", stuff[1])
print("\tCoefficient 2:",stuff[2],"\n")

print("Consecutive Integer Checking Algorithm: gcd(",m,",",n,") = ",CICA(m,n),"\n")

print("Middle school procedure:  gcd(",m,",",n,") = ",middleSchoolProcedure(m,n))
