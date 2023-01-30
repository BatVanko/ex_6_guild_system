from ex_6_guild_system.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player} is already in the guild."
        if player.guild != self.name and not player.guild == "Unaffiliated":
            return f"Player {player} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player_name)
        player_name.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        if self.players:
            for player in self.players:
                result += player.player_info()
        return result

