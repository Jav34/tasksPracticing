"""nie uproszczona wersja"""

cena = 1200
bon = 100
przyznany_bon = True

if przyznany_bon:
    cena -= bon

print(cena)

'''uproszczona wersja'''
cena = 1200
bon = 100
przyznany_bon = True

if przyznany_bon: cena -= bon, print(cena)