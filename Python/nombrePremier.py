from math import sqrt

def estPremier(n):
    if(n<=1):
        return False
    i=2
    r=sqrt(n)
    while(i <= r and n%i!=0):
        i+=1
    if(i > r):
        return True
    else:
        return False


def listePremier(nb):
    liste = []
    for i in range(nb):
        n = i
        if(estPremier(n)):
            liste.append(n)
    print(liste)


listePremier(100)