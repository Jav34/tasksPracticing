import os
import urllib.request

data_dir = r'C:\Users\JAVIER\Desktop\Javier\NaukaPython\notes.txt'

pages = [
    {'nazwa': 'abc', 'url': 'http://www.abc.com/'},
    {'nazwa': 'onet', 'url': 'http://www.onet.pl'},
    {'nazwa': 'nonexist', 'url': 'http://www.javiersito.com'}]

for page in pages:

    try:
        nazwa_pliku = "{}.html".format(pages['nazwa'])
        path = os.path.join(data_dir, nazwa_pliku)

        print('Procesuje: {} => {}...'.format(page['url'], nazwa_pliku))
        urllib.request.urlretrieve(page['url'], path)
        print('...gotowe')

    except:
        print('Błąd podczas procesowania strony: {}'.format(page['nazwa']))
        print('Koniec procesowania')
        break
else:
    print('Wszystkie strony zapisały poprawnie!!!')
