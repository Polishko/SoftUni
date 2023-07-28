from project.player import Player
from project.supply.food import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player) -> str:
        added_players = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies: Supply) -> None:
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str) -> str or None:
        player_result = [player for player in self.players if player.name == player_name]

        if not player_result or sustenance_type not in ["Food", "Drink"]:
            return

        target_player = player_result[0]

        if not target_player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply_result = [(self.supplies[i], i)
                         for i in range(len(self.supplies)) if self.supplies[i].TYPE == sustenance_type]

        if not supply_result:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        supply, i = supply_result[-1][0], supply_result[-1][1]

        target_player.stamina = min(target_player.stamina + supply.energy, 100)
        del self.supplies[i]

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str or None:
        player_1 = [player for player in self.players if player.name == first_player_name][0]
        player_2 = [player for player in self.players if player.name == second_player_name][0]

        zero_stamina = [f"Player {player.name} does not have enough stamina."
                        for player in [player_1, player_2] if player.stamina == 0]
        if zero_stamina:
            return "\n".join(zero_stamina)

        if player_1.stamina > player_2.stamina:
            player_1, player_2 = player_2, player_1

        for player in [player_1, player_2]:
            attacked = player_2 if player == player_1 else player_1
            stamina = attacked.stamina - player.stamina / 2

            if stamina <= 0:
                attacked.stamina = 0
                return f"Winner: {player.name}"
            else:
                attacked.stamina = stamina

        winner = player_1 if player_1.stamina > player_2.stamina else player_2
        return f"Winner: {winner.name}"

    def next_day(self) -> None:
        for player in self.players:
            new_stamina = player.stamina - player.age * 2
            player.stamina = new_stamina if new_stamina > 0 else 0

        for player in self.players:
            for food in ("Food", "Drink"):
                self.sustain(player.name, food)

    def __str__(self):
        result = []

        [result.append(str(player)) for player in self.players]
        [result.append(supply.details()) for supply in self.supplies]

        return "\n".join(result)


