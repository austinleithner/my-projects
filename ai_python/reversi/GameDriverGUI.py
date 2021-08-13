from Game import *
from Players import *
#from BasicAshbyAgent import BasicAgent

if __name__ == "__main__":
    game = Game(Human(1, name="Wade"), AIAgent(2, name="Bob"), time_per_turn=1, gui=True)
    game.start_game()
