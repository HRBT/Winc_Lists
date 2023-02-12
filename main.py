# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# Exercise 1

a = ['The Poseidon Adventure',
'Cinderella Liberty',
'Tom Sawyer',
'Earthquake',
'Jaws',
'Close Encounters of the Third Kind',
'Star Wars: Episode IV',
'Superman',
'Star Wars: Episode V – The Empire Strikes Back',
'E.T. the Extra-Terrestrial',
'If We Were in Love',
'The River',
'Empire of the Sun',
'The Accidental Tourist',
'Born on the Fourth of July',
"Schindler's List",
'Moonlight',
'Seven Years in Tibet',
'Saving Private Ryan',
"Angela's Ashes",
'A.I. Artificial Intelligence',
'Memoirs of a Geisha',
'War Horse',
'Lincoln',
'The Book Thief',
'The Post',
'The Fabelmans']

def alphabetical_order(x):
    alpha_sorted_list = sorted(x)
    return(alpha_sorted_list)

alphabetical_order(a)

print()


# Exercise 2

lower_a = ['The Poseidon Adventure',
'Cinderella Liberty',
'Tom Sawyer',
'Earthquake',
'Jaws',
'Close Encounters of the Third Kind',
'Star Wars: Episode IV',
'Superman',
'Star Wars: Episode V – The Empire Strikes Back',
'E.T. the Extra-Terrestrial',
'If We Were in Love',
'The River',
'Empire of the Sun',
'The Accidental Tourist',
'Born on the Fourth of July',
"Schindler's List",
'Moonlight',
'Seven Years in Tibet',
'Saving Private Ryan',
"Angela's Ashes",
'A.I. Artificial Intelligence',
'Memoirs of a Geisha',
'War Horse',
'Lincoln',
'The Book Thief',
'The Post',
'The Fabelmans']
for i in range(len(lower_a)):
    lower_a[i] = lower_a[i].lower()
print(lower_a)

print(list)

print()

list = lower_a

def won_golden_globe(x):
    if x.lower() in list:
        return(True)
    else:
        return(False)

#won_golden_globe('superman')
#won_golden_globe('celeste')
won_golden_globe('JAWS')

print()

#print('Exercise 3')

toto_albums = ['Fahrenheit', 'The Seventh ONe', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old is New']
for i in range(len(toto_albums)):
    toto_albums[i] = toto_albums[i].lower()
print(toto_albums)

print()

list_accidentally = list + toto_albums
print(list_accidentally)

print()

# print(len(toto_albums))

def remove_toto_albums(x):
    if toto_albums[0] in x:
        x.remove(toto_albums[0])
    if toto_albums[1] in x:
        x.remove(toto_albums[1])
    if toto_albums[2] in x:
        x.remove(toto_albums[2])
    if toto_albums[3] in x:
        x.remove(toto_albums[3])
    if toto_albums[4] in x:
        x.remove(toto_albums[4])
    if toto_albums[5] in x:
        x.remove(toto_albums[5])
    return(list_accidentally)
       
#remove_toto_albums(list_accidentally)
print(remove_toto_albums(list_accidentally))
 