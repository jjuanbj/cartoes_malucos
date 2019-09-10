class Player:
    def __init__(self, name, state):
        self.name = name
        self.state = state


p = Player
p.name = 'Juan'
p.state = 1

print(p.name, str(p.state))
