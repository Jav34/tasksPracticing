import os

ścieżka = r'C:\Users\JAVIER\Desktop\Javier\NaukaPython\notes.txt'

def TworzymyPlik(ścieżka):
    with open("notes.txt") as f:
        file = f.read()
        rozbijText = file.split()
        policzText = len(rozbijText)
        listaLiter = list(file.replace(" ", ""))
        lenLista = len(listaLiter)
        print('En el texto hay {} palabras, que en total nos da {} letras'.format(policzText, lenLista))

TworzymyPlik(ścieżka)

