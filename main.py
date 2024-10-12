import requests

# Function to fetch Pokémon data from the API
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to print Pokémon details (name, abilities, and weight)
def print_pokemon_details(pokemon):
    name = pokemon['name']
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    weight = pokemon['weight']
    print(f"Name: {name}")
    print(f"Abilities: {abilities}")
    print(f"Weight: {weight}")

# Function to calculate the average weight of a list of Pokémon
def find_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    average_weight = total_weight / len(pokemon_list)
    return average_weight

# Fetch data for Pikachu, Bulbasaur, and Charmander
pikachu = fetch_pokemon_data("pikachu")
bulbasaur = fetch_pokemon_data("bulbasaur")
charmander = fetch_pokemon_data("charmander")

# Store the Pokémon data in a list
pokemon_list = [pikachu, bulbasaur, charmander]

# Print the details of each Pokémon
print_pokemon_details(pikachu)
print_pokemon_details(bulbasaur)
print_pokemon_details(charmander)

# Calculate and print the average weight
average_weight = find_average_weight(pokemon_list)
print(f"\nAverage Weight: {average_weight}")
