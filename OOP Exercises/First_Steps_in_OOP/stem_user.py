from typing import List


class SteamUser:
    def __init__(self, username: str, games: List[str]):
        self.username = username
        self.games = games
        self.played_hours: int = 0

    def play(self, game: str, hours) -> str:
        if game not in self.games:
            return f"{game} is not in library"

        self.played_hours += hours

        return f"{self.username} is playing {game}"

    def buy_game(self, game: str) -> str:
        if game in self.games:
            return f"{game} is already in your library"

        self.games.append(game)

        return f"{self.username} bought {game}"

    def status(self) -> str:
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
        
# class SteamUser:
#     def __init__(self, username, games, played_hours=0):
#         self.username = username
#         self.games = games
#         self.played_hours = played_hours

#     def play(self, game, hours):
#         if game in self.games:
#             self.played_hours += hours
#             return f"{self.username} is playing {game}"
#         else:
#             return f"{game} is not in library"

#     def buy_game(self, game):
#         if game not in self.games:
#             self.games.append(game)
#             return f"{self.username} bought {game}"
#         else:
#             return f"{game} is already in your library"

#     def status(self):
#         return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
