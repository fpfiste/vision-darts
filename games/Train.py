import numpy as np
import pyfiglet
from .BaseGame import BaseGame
import keyword

class Train(BaseGame):
    def __init__(self):
        self.shot_counter = 0
        self.on_target = 0
        super(Train).__init__()
        print(pyfiglet.figlet_format("Train Mode"))


    def sample(self):
        value = np.random.choice(self.fields)
        if value not in ('25', '50'):
            multiplier = np.random.choice(self.multipliers, p=[0.5,0.25,0.25])
        return value, multiplier

    def play(self):
        while True:
            print(100*'-')
            self.play_round()
            print('Total shots: ', self.shot_counter, '\n', 'Shots on target: ', self.on_target)
            next = input('Press any Enter to continue and q to quit ')


            if next == 'q':
                print(100 * '-')
                break

    def play_round(self):
        value, multiplier = self.sample()

        print('Target: ', multiplier + value)

        hit = input('Did you hit the target?')

        if hit == 'yes':
            self.shot_counter += 1
            self.on_target += 1
            print('Good job!')
        else:
            self.shot_counter += 1
            print('Next time!')


if __name__ == '__main__':
    game = Train()

    game.play_round()


