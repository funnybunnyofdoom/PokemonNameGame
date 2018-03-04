#This program will ask the user to name all 150 pokemon
def main():
    guessed = 0
    missed = 0
    
    PokemonList = getPkmn()    
    length = len(PokemonList)

    while guessed < length:
        PokemonName = ask()
        b = checkList(PokemonList,PokemonName)
        if b == True:
            guessed +=1
        else:
            missed +=1
    


def getPkmn():
    pkmnList = {}
    file = open('pkmn.txt','r')
    index = 0
    for line in file:
        pkmnList[index] = line
        index +=1
    file.close()
    return pkmnList




def checkList(List,pokemon):
    if pokemon in List:
        List.remove(pokemon)
        print("Congratulations! Only ",len(List),"/150 to go!")
        return True
    else:
        print("I'm sorry! Try again")
        return False

def ask():
    print("Please enter the name of a pokemon!")
    print("Please capitalize the first letter")
    pokemonName = input()
    return pokemonName

main()

