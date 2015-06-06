#Finding GCD of 2 numbers
def getGCD( a,b ):
    gcd = 1
    for i in range(0,min(a,b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

#Finding GCD of two numbers according to Euclidean formula
#This is based on the fact that the GCD will also divide the difference between the two numbers
def getGCD( a, b ):
    while b != 0:
        a,b = b, a%b
    return a

#Finding LCM of 2 numbers
def getLCM( a,b ):
    i = max(a,b)
    while True:
        if i % a == 0 and i % b == 0:
            lcm = i
    return lcm

#Finding LCM based on the GCD
def getLCM( a, b ):
    return a * b / getGCD(a,b)
