from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

# Play games and print results
print("Playing against Quincy")
print(play(player, quincy, 1000, verbose=True))
print("Playing against Mrugesh")
print(play(player, mrugesh, 1000, verbose=True))
print("Playing against Kris")
print(play(player, kris, 1000, verbose=True))
print("Playing against Abbey")
print(play(player, abbey, 1000, verbose=True))

# Uncomment the line below to run the unit tests
# unittest.main(argv=['first-arg-is-ignored'], exit=False)
