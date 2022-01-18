'''
1.1 Feladat
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

'''

"""
lista = []
while True:
    
    szam = input("kérek egy szamot: ")
    if szam != "":
        lista.append(szam)
    else:
        lista.sort(key = int)
        print(lista)
        break
print("a legnagyobb szám: ", max(lista), "a legkissebb szám a :", min(lista),"a lista pedig: ", lista)

"""
lista = []
while True:
    szam = input("kérek egy szamot: ")
    if szam == "":
        break
    else:
        szam = int(szam)
        lista.append(szam)

legkisebb = lista[0]
for i in lista:
    if i < legkisebb:
        legkisebb = i
print(legkisebb)

legnagyobb = lista[0]
for i in lista:
    if i > legnagyobb:
        legnagyobb = i
print(legnagyobb)

print("a legkisebb szám: ", legkisebb, "a legnagyobb szám a :", legnagyobb,"a lista pedig: ", lista)


