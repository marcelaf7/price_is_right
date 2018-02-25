from Player import Player
from randItem import RandAmazon


class Game:

    def __init__(self):
        self.amazon_items = RandAmazon('AmazonData.JSON')
        self.player_list = []
        self.num_players = 0
        self.price = 20

    def play_game(self):
        self.item = self.amazon_items.generateRand()
        self.price = self.item['Price']

        print('Welcome to Price is Right: The Game!')
        self.num_players = self.get_number_players()
        self.create_players_and_guess()
        self.display_player_guesses()
        self.display_winners()

    def create_players_and_guess(self):
        for i in range(self.num_players):
            current_player = Player(i + 1)
            print('Player', current_player.ID, 'is up')
            current_player.guess = int(input('Please enter a price: '))
            self.player_list.append(current_player)

    def display_player_guesses(self):
        for player in self.player_list:
            print('Player', player.ID, 'guessed: ', player.guess)

    def display_winners(self):
        guess_differences = [abs(player.guess - self.price) for player in self.player_list]
        indices = [i + 1 for i, x in enumerate(guess_differences) if x == min(guess_differences)]
        indices = ', '.join(str(e) for e in indices)

        print('Actual price of', self.item['Title'], 'was', self.price)
        print('Player(s)', indices, 'have won the game!')

    def get_number_players(self):
        while True:
            num_players = input('Please enter number of players (2-4): ')
            try:
                num_players = int(num_players)
                if num_players < 2 or num_players > 4:
                    continue
                else:
                    return num_players
            except ValueError:
                print('Bruh, I just said 2-4')

game = Game()
game.play_game()