# africa_game
import random as r
import time as t
countries = ['algeria', 'angola', 'benin', 'botswana', 'burkina faso', 'burundi', 'cabo verde', 'cameroon', 'central african republic', 'chad', 'comoros', 'ivory coast', 'djibouti', 'democratic republic of the congo', 'egypt', 'equatorial guinea', 'eritrea', 'eswatini', 'ethiopia', 'gabon', 'gambia', 'ghana', 'guinea', 'guinea-bissau', 'kenya', 'lesotho', 'liberia', 'libya', 'madagascar', 'malawi', 'mali', 'mauritania', 'mauritius', 'morocco', 'mozambique', 'namibia', 'niger', 'nigeria', 'republic of the congo', 'rwanda', 'sao tome &principe', 'senegal', 'seychelles', 'sierra leone', 'somalia', 'south africa', 'south sudan', 'sudan', 'tanzania', 'togo', 'tunisia', 'uganda', 'zambia', 'zimbabwe' ]
named = []
print('---COUNTRIES OF AFRICA---\n\n*Note:	To check the countries you\'ve named, type \'named\'\n	Hints available after score 15\n')
score = 0
hintcount = 0
while len(countries) >0:
    print('Number of countries to guess:', len(countries))
    print('score:',score)
    if hintcount > 0:
        print('hints used:',hintcount)
    if score < 15:
        country = input('name a country in africa: ')
    else:
        country = input('name a country in africa (type "hint" to recieve a hint): ')
    country = country.lower()
    if country in countries:
        print('good guess')
        score += 1
        named.append(country)
        countries.remove(country)
    elif country in named:
        print('you already named this country')
    elif country == 'named':
        print('')
        print(*named,'\n')
    elif country == 'hint':
        country = r.choice(countries)
        print(f'the country "{country}" has been revealed for you')
        hintcount += 1
        named.append(country)
        countries.remove(country)
    else:
        print('invalid guess')
        print('try again')
    t.sleep(0.7)
    print('\n')
if len(countries) == 0:
    print('WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nGood game')
    print('score:',score)
    print('hints used:',hintcount)
