def DisplayOptions(options):
    for i in range(len(options)): #iloraz powtórzeń, równa ilości obiektów na liście
        print('{} - {}'.format(i+1, options[i])) #w klamrach pojawią się obiekty we wskazanym formacie w którym i+1 pokaże liczę 1 zamiast 0

    choice = input('Select option above or press enter to exit: ')
    return choice

choice = 'x' #tworzymy zmienną do której zwrócić się w pętli while
options = ['Load data', 'Export data', 'Analyze & Predict']

while choice: #powstaje pętla while
    choice = DisplayOptions(options) #zmieniamy zawartość zmiennej na utworzoną Funkcję


    if choice: #czyli, dopóki input nie jest empty
        try: #spróbuj to:
            choice_num = int(choice)-1 #to ponieważ python zaczyna od 0, nie od 1
            if choice_num >= 0 and choice_num < len(options):
                print('You have selected {} - {}'.format(choice_num+1, options[choice_num]))
            else:
                print('Choose a value from a list or press enter')
        except:
            print('You need to enter a number')
    else:
        print("----END----")



