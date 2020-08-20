import time

#Plik 1 -----
plik_s = input("Ścieżka do pliku z danymi wejściowymi: ")

#usuwanie "Windowsowych" sleshy (zm. na odpowiednie)
for u in range(len(plik_s)):   
    if chr(92) == plik_s[u]:
        plik_s = plik_s[:u] + "/" + plik_s[u + 1:]

plik = open(plik_s)
plik_l = plik.readlines()
plik.close()

inp = plik_l[0]

#Plik 2 -----
plik_s = input("Ścieżka do pliku z danymi wyjściowymi: ")

for u in range(len(plik_s)):   
    if chr(92) == plik_s[u]:
        plik_s = plik_s[:u] + "/" + plik_s[u + 1:]

plik2 = open(plik_s)
plik2_odp = plik2.readlines()
plik2.close()

ODP = int(plik2_odp[0])

czas1 = time.time()#Stoper - start

#------
zakryj = 0
ost = ""

for i in range(len(inp)):
    if inp[i] == ost:
        zakryj += 1
    ost = inp[i]

wynik = int(zakryj)
#------

#Podsumowanie
czas2 = time.time()
czas3 = czas2 - czas1

if wynik == ODP:
    print("Dobrze!!!")
    print("Czas: " + str(czas3))
    print("Odp: " + str(wynik))
else:
    print("Dobrze!!!")
    print("Czas: " + str(czas3))
    print("Odp: " + str(wynik))