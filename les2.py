scissors = 0
paper = 1
stone = 2

player_1 = scissors
player_2 = stone

if player_1 > player_2 :
    print("Player 1 win")
elif player_1 < player_2 :
    print("Player 2 win")
else :
    print("Draw")


  \\\  ___________________________

    s = 'Hello'
    print(s[0])
    print(s[:2])

    l = ['a', 'b', 1, 2, 3.2]
    l.append('c')
    print(l)

    d = {'a': [1, 2, 3], 'b': "bd", 'c': 'df'}
    d['a1'] = 'a1'

    print(type(d['a']))
    print(d.get('a'))
    print(d['a'].append(4))
    print(d['a'][0])
    print(d)

\\\