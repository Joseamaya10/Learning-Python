class PartyAnimal:
    def __init__(self, nam):
        self.name = nam
        self.x = 0
        print(self.name, "construido")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()