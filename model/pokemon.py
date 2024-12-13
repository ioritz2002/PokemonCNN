
class Pokemon:
    def __init__(self, name, pokemon_id, height, weight, abilities, types, debilities, evolution_chain):
        self.name = name
        self.pokemon_id = pokemon_id
        self.height = height
        self.weight = weight
        self.abilities = abilities
        self.types = types
        self.debilities = debilities
        self.evolution_chain = evolution_chain

    def showData(self):
        print("Pokemon ID: " + str(self.pokemon_id))
        print("Name: " + self.name)
        print("Height: " + str(self.height))
        print("Weight: " + str(self.weight))
        print("Habilities: " + self.abilities)
        print("Type: " + self.types)
        print("Is weak against: " + self.debilities)
        print("The evolution chain is:" + self.evolution_chain)
