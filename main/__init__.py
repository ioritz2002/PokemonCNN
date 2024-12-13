from model.data_fetcher import fetch_pokemon_data


pokemon_name = "empoleon"
pokemon = fetch_pokemon_data(pokemon_name)

if pokemon:
  pokemon.showData()