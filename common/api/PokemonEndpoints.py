class PokemonEndpoints:

    def __init__(self):
        pass

    def pokemon_name_resource(self, pokemon_name):
        return f"pokemon/{pokemon_name}"

    def pokemon_type_base_resource(self, pokemon_type):
        return f'type/{pokemon_type}'

    def pokemon_ability_base_resource(self, pokemon_ability):
        return f'ability/{pokemon_ability}'

    def pokemon_berries_base_resource(self, pokemon_berry):
        return f'berry/{pokemon_berry}'
