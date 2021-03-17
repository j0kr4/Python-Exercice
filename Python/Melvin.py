# La bataille sans bataille

import random

#creation du paquet de carte
paquet=[]
for i in range(1,21):
    paquet=paquet+[i]

# melange des cartes en repetant 50 fois un échange de 2 cartes choisies aleatoirement
for k in range(50):
    i=random.randint(0,19)
    j=random.randint(0,19)
    temp=paquet[i]
    paquet[i]=paquet[j]
    paquet[j]=temp

# distribution
paquetA=20*[0]
paquetB=20*[0]
for i in range(10):
    paquetA[i]=paquet[2*i]
    paquetB[i]=paquet[2*i+1]

# retirer le Premier Element d'une liste
def retirerPremierElement1(paq):
    n = len(L)
    Lbis = n*[0]
    for i in range(1, n):
        Lbis[i-1]=L[i]
    return Lbis

#retourne l'indice de la première occurence de 0
def indiceZero(paq):
    i = 0
    n = len(L)
    while i<n and L[i]!=0:
        i = i+1
    return i
ZeroA = indiceZero(paquetA)
ZeroB = indiceZero(paquetB)
if ZeroA!=len(paquetA):
    print("Le premier 0 se trouve à l'indice : ", ZeroA)
else:
    print(len(paquetA))
if ZeroB!=len(paquetB):
    print("Le premier 0 se trouve à l'indice : ", ZeroB)
else:
    print(len(paquetB))



#comparer les cartes d'un pli
def pli(paq):
    carteA = paquetA[0]
    carteB = paquetB[0]
    print("A joue : ", carteA)
    print("B joue : ", carteB)
    if carteA>carteB:
        paquetA[ZeroA].append(carteB, carteA)

        print("A emporte le pli")
    else:
        paquetB[ZeroB].append(carteA, carteB)
        print("B emporte le pli")


#La fonction RangZero retourne l'indice de la premiere occurence de 0 dans le tableau paq,
# et retourne 20 si aucun 0 n'est trouve
def RangZero(paq):



print("paquet après mélange :",paquet,"\n")
print("\t","paquet du joueur A :",paquetA)
print("\t","paquet du joueur B :",paquetB)

print("\n\t\t\tDébut du jeu\n")