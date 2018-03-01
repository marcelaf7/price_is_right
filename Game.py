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
        self.setup_players()
        self.display_item()
        self.let_players_guess()
        self.display_player_guesses()
        self.display_winners()

    def display_item(self):
        print('You are bidding on \n\t', self.item['Title'])
        print(self.item['Image'])

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

    def setup_players(self):
        for i in range(self.num_players):
            username = input('Please enter a username for player %d: ' % (i + 1))
            self.player_list.append(Player(username))

    def let_players_guess(self):
        for player in self.player_list:
            print(player.username, 'is up')
            player.guess = int(input('Please enter a price:'))

    def display_player_guesses(self):
        for player in self.player_list:
            print('Player', player.username, 'guessed: ', player.guess)

    def display_winners(self):
        guess_differences = [abs(player.guess - self.price) for player in self.player_list]
        indices = [i for i, x in enumerate(guess_differences) if x == min(guess_differences)]

        print('Actual price of', self.item['Title'], 'was', self.price)

        if len(indices) == 1:
            print(self.player_list[indices[0]].username, 'has won the game!')
            self.player_list[indices[0]].score += 1
        else:
            winning_usernames = [player.username for i, player in enumerate(self.player_list) if i in indices]
            winning_usernames = ', '.join(str(e) for e in winning_usernames)
            print(winning_usernames, 'have won the game!')
            for i, player in enumerate(self.player_list):
                if i in indices:
                    player.score += 1

    def get_image_url(self):
        return self.item['URL']

game = Game()
game.play_game()