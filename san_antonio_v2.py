from random import randint
import json

#quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !","On doit pouvoir choisir entre s'écouter parler et se faire entendre.","Mais qui va là, jeune padawan du Python Monthy!","Quoi, un full stack, baby il faut y aller.","Nova, les US sont plus dans le futur que nous?!"]
#characters = ["alvin et les Chipmunks","Babar","betty boop","calimero","casper","le chat potté","Kirikou"]

#Values form JSON file
def read_values_from_json(file, key):
  values = []
  with open(file) as c: #fichier ouvert nommé c dans le code
    data = json.load(c) #data = chargement des données de f (via fct° load du module json)
    for entry in data: #pour chaque entrée de data
      values.append(entry[key]) #ajouter entrée si elle a "character" comme clé (dans le JSON)
    return values

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character,n_quote)

def show_random_item(my_list):
    index=randint(0,len(my_list)-1)
    item = my_list[index] 
    return item

def random_character():
    all_characters = read_values_from_json('characters.json','character')
    return show_random_item(all_characters)

def random_quote():
    all_quotes = read_values_from_json('quotes.json','quote')
    return show_random_item(all_quotes)
 

a = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

while a != "B":
  print(message(random_character(), random_quote()))
  a = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')

    
#for i in characters:
    #maj_i=i.capitalize()
    #print(maj_i)



