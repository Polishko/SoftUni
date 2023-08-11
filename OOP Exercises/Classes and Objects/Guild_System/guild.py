from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = set()

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.add(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        copy_players = self.players.copy()

        for person in copy_players:
            if person.name == player_name:
                self.players.remove(person)
                person.guild = "Unaffiliated"

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = []
        result.append(f"Guild: {self.name}")

        for person in self.players:
            result.append(f"{person.player_info()}")

        return "\n".join(result)
