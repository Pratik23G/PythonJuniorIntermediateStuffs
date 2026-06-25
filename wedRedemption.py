#today quick recap on OOP in python

class Players:
    def __init__(self, player_name:str, player_age:int, net_worth: int):
        self.player_name = player_name
        self.player_age = player_age
        self._net_worth = net_worth #This is private can't be accessed easily

    def display_stat(self) -> str:
        return f"{self.player_name}, who is {self.player_age}, earns the most"


class ArgentinaPlayer(Players):
    def __init__(self, player_name: str, player_age: int):
        super().__init__(player_name, player_age, 10000000000000)
        self.tricks :list[str] = []
        self.tricks.append("Body Fient")
        self.tricks.append("8 balloon Do'r")
        self.tricks.append("Finesse Shot")

    def display_stat(self) -> str: # This is polymorphism (overrides the original value class Players has)
        return f"{self.player_name}, who is {self.player_age}, earns a lot & can do these tricks: {','.join(self.tricks)}"

class BrazilPlayer(Players):
    def __init__(self, player_name: str, player_age: int):
        super().__init__(player_name, player_age, 20000000000)

WorldCupStar = Players("Messi", 39, 45000000000)

WorldCupStar.display_stat()

for player in [BrazilPlayer("Neymar", 30), ArgentinaPlayer("Messi", 39)]:
    print(player.display_stat())