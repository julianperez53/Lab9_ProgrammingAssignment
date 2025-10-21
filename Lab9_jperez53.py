'''2-player game about flipping coins.
    Match Coins
    Author: Julian Perez
    Date: 10/21/2025
'''

import random

#Class used to create both player's coin amounts and toss coins.
class Coin:
    def __init__(self, __amount=20, __sideup='Heads') -> None:
        self.__amount = __amount
        self.__sideup = __sideup
    def toss(self):
        side = random.choice(['0', '1'])
        if side == '0':
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    def get_sideup(self):
        return f"{self.__sideup}"
    def get_amount(self):
        return f"{self.__amount}"
    def set_amount(self, int):
        self.__amount += int

#Intro paragraph for instructions
winner = ''
print('Welcome to Match Coins. This is a two-player game where both players flip a coin.')
print('If both coins match, Player 1 steals a coin from Player 2. Otherwise, Player 2 steals a coin from Player 1.')
print('Whoever loses all coins loses, or if the game ends prematurely, whoever has the most coins at the end of the game wins.\nBoth players start with 20 coins.')
print('May the odds be ever in your favor!\n')

def main():
    #init both players' coins using Coin class
    player1_coin = Coin()
    player2_coin = Coin()
    keep_playing = 'Y'
    while keep_playing == 'Y':
        keep_playing = input('Do you want to play Match Coins? Y for yes, any other key for no.\n').upper()
        if keep_playing == 'Y':
            #tosses both coins and displays results
            player1_coin.toss()
            player2_coin.toss()
            print(f'Player 1 coin: {player1_coin.get_sideup()}\nPlayer 2 coin: {player2_coin.get_sideup()}')

            #depending on sideup, one player steals the other's coin then displays results
            if player1_coin.get_sideup() == player2_coin.get_sideup():
                player1_coin.set_amount(1)
                player2_coin.set_amount(-1)
            else:
                player2_coin.set_amount(1)
                player1_coin.set_amount(-1)
            print(f'Player 1 coin amount: {player1_coin.get_amount()}\nPlayer 2 coin amount: {player2_coin.get_amount()}')

            #game over if one player has no coins
            if player1_coin.get_amount() == '0':
                print(f'Player 1 has no more coins.\nPlayer 2 wins!')
                keep_playing = 'N'
            elif player2_coin.get_amount() == '0':
                print(f'Player 2 has no more coins.\nPlayer 1 wins!')
                keep_playing = 'N'

    #to call out winning player for closing statement
    player1Amount = int(player1_coin.get_amount())
    player2Amount = int(player2_coin.get_amount())
    if player1Amount > player2Amount:
        winner = 'Player 1'
    elif player2Amount > player1Amount:
        winner = 'Player 2'
    else:
        winner = 'neither player'
    
    #closing statement
    print(f'Thanks so much for playing Match Coins, and congrats to {winner} for winning! Have a great day!')

main()