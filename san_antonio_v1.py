from random import randint

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
    "Mais qui va là, jeune padawan du Python Monthy!",
    "Quoi, un full stack, baby il faut y aller.",
    "Nova, les US sont plus dans le futur que nous?!"
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]


def show_random_item(my_list):
    index=randint(0,len(my_list)-1)
    item = my_list[index] 
    return item
 

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character,n_quote)


a = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

while a != "B":
  print(message(show_random_item(characters), show_random_item(quotes)))
  a = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

    
#for i in characters:
    #maj_i=i.capitalize()
    #print(maj_i)



