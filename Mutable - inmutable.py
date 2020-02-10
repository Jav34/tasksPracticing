dni = ['pon', 'wto', 'śrd', 'czw', 'pt', 'sob', 'niedz']
dni_pracujące = ['pon', 'wto', 'śrd', 'czw', 'pt', 'sob', 'niedz']
dni_pracujące.remove('sob')
dni_pracujące.remove('niedz')
print('Oto dni tygodnia:', dni)
print('A w tych dniach pracujemy: ', dni_pracujące)
