
Kaas1 = input('Is de kaas geel? ' )
if Kaas1 == 'ja':
    Kaas2 = input('Zitten er gaten in? ' )
    if Kaas2 == 'ja':
        Kaas3 = input('Is de kaas belachelijk duur? ')
    elif Kaas2 == 'nee':
        Kaas4 = input('Is de kaas hard als steen? ') 
        if Kaas4 == 'ja':
            print('Parmigiano Reggiano')
        elif Kaas4 == 'nee':
            print('Goudse Kaas')
    if Kaas3 == 'ja':
                print('Emmenthaler')
    elif Kaas3 == 'nee':
                print('Leerdammer')
elif Kaas1 == 'nee':
        Kaas2 = input('Heeft de kaas blauwe schimmels? ')
        if Kaas2 == 'ja':
            Kaas3 = input('Heeft de kaas een korst? ')
        elif Kaas2 == 'nee':
            Kaas4 = input('Heeft de kaas een korst? ')
            if Kaas4 == 'ja':
                print('Cammembert')
            elif Kaas4 == 'nee':
                print('Mozzerella')
        if Kaas3 == 'ja':
            print('Blue de Rochbaron')
        elif Kaas3 == 'nee':
            print('Foume d\'Ambert')