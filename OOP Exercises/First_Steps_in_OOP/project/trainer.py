from project.pokemon import Pokemon
from typing import List


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)

                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

        # can use try except (stop iteration error) with filter looking for pokemon_name

    def trainer_data(self) -> str:
        pokemon_data = "\n".join([f"- {p.pokemon_details()}" for p in self.pokemons])
        return f"Pokemon Trainer {self.name}\n"\
            + f"Pokemon count {len(self.pokemons)}\n"\
            + f"{pokemon_data}"
