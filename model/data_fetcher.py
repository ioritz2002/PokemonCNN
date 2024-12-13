import requests
from model.pokemon import Pokemon

url_pokemon = "https://pokeapi.co/api/v2/pokemon/"
url_evolution = "https://pokeapi.co/api/v2/evolution-chain/"
url_types = "https://pokeapi.co/api/v2/type/"

def getEvolutionChain(pokemon_data):
    try:
        species_url = pokemon_data['species']['url']
        species_data = requests.get(species_url).json()
        evolution_chain_url = species_data['evolution_chain']['url']
        evolution_chain_data = requests.get(evolution_chain_url).json()

        evolution_chain = []
        current_evolution = evolution_chain_data['chain']

        while current_evolution:
            evolution_chain.append(current_evolution['species']['name'])
            if 'evolves_to' in current_evolution and current_evolution['evolves_to']:
                current_evolution = current_evolution['evolves_to'][0]
            else:
                current_evolution = None

        if len(evolution_chain) == 1 and evolution_chain[0] == pokemon_data['name'] :
            return None

        return evolution_chain
    except Exception as e:
        print(f"Error al obtener la informacion de la cadena de evolucion: {e}")
        return None

def getDebilities(type_name):
    try:
        type_debilities = requests.get(f"{url_types}{type_name}").json()
        return type_debilities['damage_relations']['double_damage_from'][0]['name']
    except Exception as e:
        print(f"Error al obtener la informacion de las debilidades del pokemon: {e}")
        return None

def fetch_pokemon_data(pokemon_name):
    try:
        pokemon_data = requests.get(f"{url_pokemon}{pokemon_name}").json()

        name = pokemon_data['name']
        poke_id = pokemon_data['id']
        height = pokemon_data['height']
        weight = pokemon_data['weight']
        abilities = []
        types = []
        debilities = []


        for ability in pokemon_data['abilities']:
            abilities.append(ability['ability']['name'])


        for type in pokemon_data['types']:
            types.append(type['type']['name'])

        for type in types:
            debility = getDebilities(type)
            debilities.append(debility)


        evolution_chain = getEvolutionChain(pokemon_data)


        return Pokemon(name, poke_id, height, weight, abilities.__str__(), types.__str__(), debilities.__str__(), evolution_chain.__str__())
    except Exception as e:
        print(f"Error al obtener la informacion del Pokemon: {e}")
        return None