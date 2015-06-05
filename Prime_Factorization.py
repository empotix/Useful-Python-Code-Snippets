#Iterates upto the number itself
def getPrimeFactorsSum(num):
    d = 2
    factors = []
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num = num//d
        d += 1

#Improves on the performance
def getPrimeFactorsSum(num):
    d = 2
    factors = []
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num = num//d
        d += 1
        if d**2 > num:
            factors.append(num)
            break
