def retirerPremierElement(L):
    Lbis=[]
    n = len(L)
    for i in range(1, n):
        Lbis.append(L[i])
    return Lbis

def retirerPremierElement1(L):
    n = len(L)
    Lbis = n*[0]
    for i in range(1, n):
        Lbis[i-1]=L[i]
    return Lbis

def indiceZero(L):
    #retourne l'indice de la première occurence de 0
    i = 0
    n = len(L)
    while i<n and L[i]!=0:
        i = i+1
    return i


Liste = [i+1 for i in range(10)]
Liste1 = [4, 5, 9, 6, 4, 4, 2]
L = retirerPremierElement(Liste)
L1 = retirerPremierElement1(Liste)
Zero = indiceZero(Liste1)
if Zero!=len(Liste1):
    print("Le premier 0 se trouve en position : ", Zero+1)
else:
    print(len(Liste1))

