class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.current_index = 0
        return self

    def get_player(self, current_index):
        return self.players[current_index]

    def __next__(self):
        if self.current_index < self.last_player_index:            
            player = self.get_player(self.current_index)
            self.current_index += 1
            return player
        elif self.current_index == self.last_player_index:
            player = self.get_player(self.current_index)
            self.current_index = 0
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))



