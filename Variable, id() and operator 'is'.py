a = b = c = 10
print(id(a), id(b), id(c))
print('*'*8)
#w pierwszym przykładzie wszystkie zmienne mają ten sam identificator

a = 20
print(id(a), id(b), id(c))
print('*'*8)
# w drugim przykładzie, zmienna a ma już inny id

a = b = c = 20, 11, 2
print(id(a), id(b), id(c))
print('*'*8)
# wreszcie wszystkie id różnią się

a = b = c = [1, 2, 3]
print(id(a), id(b), id(c))
a.append(4)
print(a)
print('*'*8)

x = 10
y = 10 + 1234567890 - 123456789
print(id(x), id(x))


