import pyfiglet

from games import BaseGame


class G301(BaseGame):
    def __init__(self,):
        self.state = {}
        print(pyfiglet.figlet_format("Train Mode"))


    def setup(self):
        while True:
            player = input('Insert the next Player. ')
            self.state[player] = 301

            if input('Insert more players? ').lower() in ('no', 'n'):
                break
        if input('Do you want to finish with double out? ') in ('yes', 'y'):
            self.double_out = True
        else:
            self.double_out = False

    def get_input(self, player):
        while True:
            score = input(f'please enter the score of your throw. ').strip()
            if (len(score) > 3) or (score[0].lower() not in ['s', 'd', 't'])  or (score[1:].isnumeric() == False) or (score[1:] not in self.fields):
                print('The input has to follow the format where the first characters defines the multiplier and the 2 following digits the fields on the darts board.\n Example: S20, D15, etc')
            else:
                multiplier = score[0].lower()
                field = int(score[1:])



                return multiplier, field


    def play_round(self):
        turn = 0
        while turn < len(self.state.keys()):
            player = list(self.state.keys())[turn]
            tmp_state = self.state[player]
            persist = True
            print(f'\n{player}\thas {tmp_state} points left! ')
            for i in range(1, 4):
                multiplier, field = self.get_input(player)

                if field in (25, 50):
                    score = field
                elif multiplier == 'd':
                    score = field * 2
                elif multiplier == 't':
                    score = field * 3
                else:
                    score = field

                tmp_state -= score

                if (tmp_state < 0) or (tmp_state <= 1 and self.double_out == True and multiplier != 'd'):
                    print('Over thrown! ')
                    print(f'{player} has {self.state[player]} points left! ')
                    persist=False
                    break
                elif tmp_state == 0:
                    print('You win!')
                    return
                else:
                    print(f'{player} has {tmp_state} points left! ')

            if persist:
                self.state[player] = tmp_state
            turn += 1


    def play(self):
        self.setup()

        while True:
            result = self.play_round()
            print(100 * '-')

            if result:
                break

