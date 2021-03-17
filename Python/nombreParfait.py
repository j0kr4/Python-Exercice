def sommeDiv(n):
    if n<=1:
        somme = 0
        return somme
    somme = 1
    for i in range(2,(n//2)+1):
        if(n%i == 0):
            somme = somme+i
    return somme



def estParfait(n):
    if(n<1):
        return False
    if(n == sommeDiv(n)):
        return True
    return False


def listeParfait(nb):
    liste = []
    for i in range(nb):
        n = i
        if(estParfait(n)):
            liste.append(n)
    print(liste)

listeParfait(10000)