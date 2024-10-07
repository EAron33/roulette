import random
import time
Piros=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
pirosbet=0
Fekete=[2,4,6,8,11,10,13,15,17,20,22,24,26,28,29,31,33,35]
Feketebet=0
c1=[1,4,7,10,13,16,19,22,25,28,31,34]
c1bet=0
c2=[2,5,8,11,14,17,20,23,26,29,32,35]
c2bet=0
c3=[3,6,9,12,15,18,21,24,27,30,33,36]
c3bet=0
elso18=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
elso18bet=0
utolso18=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
utolso18bet=0
elso12=[1,2,3,4,5,6,7,8,9,10,11,12]
elso12bet=0
masodik12=[13,14,15,16,17,18,19,20,21,22,23,24]
masodik12bet=0
harmadik12=[25,26,27,28,29,30,31,32,33,34,35,36]
harmadik12bet=0
tetek= []
fogadottszamok = []
bevetel = 0

while True:
    print(f"Mire szeretnél feltenni pénz?\n1. Számra [{sum(tetek)}]\n2. Feketére [{Feketebet}]\n3. Pirosra [{pirosbet}]\n4. Első oszlopra [{c1bet}]\n5. Második oszlopra [{c2bet}]\n6. Harmadik oszlopra [{c3bet}]\n7. Első tizenkettőre [{elso12bet}]\n8. Második tizenkettőre [{masodik12bet}]\n9. Harmadik tizenkettőre [{harmadik12bet}]\n10. Első félre [{elso18bet}]\n11. Második fére [{utolso18bet}]\n12. Nincs több tét")
    bevitel = int(input())
    if bevitel == 1:
        if len(fogadottszamok) > 0:
            print(f'Eddig ezekre a számokra fogadtál:')
            if len(fogadottszamok) > 0:
                for i, szam in enumerate(fogadottszamok):
                    print(f"{szam} számra {tetek[i]} zseton")
        fogadni = int(input("Melyik számra szeretnél fogadni? (0-36)"))
        tet = int(input("Mennyi zsetont szeretnél feltenni erre a számra?"))
        fogadottszamok.append(fogadni)
        tetek.append(tet)
    if bevitel==3:
        pirosbet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==4:
        c1bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==5:
        c2bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==6:
        c3bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==7:
        elso12bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==8:
        masodik12bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==9:
        harmadik12bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==10:
        elso18bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==11:
        utolso18bet += int(input("Mennyi zsetont szeretnél feltenni?"))
    if bevitel==12:
        break

sorsolt = random.randint(0,36)
print(f"A sorsolt szám {sorsolt}")

if len(fogadottszamok) > 0:
    for i,szam in enumerate(fogadottszamok):
        if szam == sorsolt:
            bevetel += tetek[i] * 35
            bevetel += tetek[i]
            fogadottszamok.pop(i)
            tetek.pop(i)
    bevetel -= sum(tetek)

if sorsolt in Fekete:
    bevetel += Feketebet *2
else:
    bevetel -= Feketebet

if sorsolt in Piros:
    bevetel += pirosbet *2
else:
    bevetel -= pirosbet

if sorsolt in c1:
    bevetel += c1bet *3
else:
    bevetel -= c1bet

if sorsolt in c2:
    bevetel += c2bet *3
else:
    bevetel -= c2bet

if sorsolt in c3:
    bevetel += c3bet *3
else:
    bevetel -= c3bet

if sorsolt in elso12:
    bevetel += elso12bet *3
else:
    bevetel -= elso12bet

if sorsolt in masodik12:
    bevetel += masodik12bet *3
else:
    bevetel -= masodik12bet

if sorsolt in harmadik12:
    bevetel += harmadik12bet *3
else:
    bevetel -= harmadik12bet

if sorsolt in elso18:
    bevetel += elso18bet *2
else:
    bevetel -= elso18bet

if sorsolt in utolso18:
    bevetel += utolso18bet *2
else:
    bevetel -= utolso18bet

print(f"Az ön bevétele ebből a játékból:{bevetel} A játék 20mp után leáll")
time.sleep(20)