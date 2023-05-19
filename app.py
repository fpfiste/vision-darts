import pyfiglet

from games import Train, G301, G501

modes = {
    '1' : G301,
    '2' : G501,
    '3' : Train
}

if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("DartsScorer!!")
    print(ascii_banner)

    while True:
        mode_options = ['301', '501', 'Train']
        input_message = "Pick an option:\n"

        for index, item in enumerate(mode_options):
            input_message += f'{index + 1}) {item}\n'

        input_message += 'Your choice: '
        mode = input(input_message)

        modes[mode]().play()
