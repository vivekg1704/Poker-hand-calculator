from itertools import product
ALLOWED_SUITS = ['H','D','C','S']
ALLOWED_NUMBERS = [i for i in range(1,14)]
ALLOWED_CARDS = list(product(ALLOWED_NUMBERS,ALLOWED_SUITS))

class Card:

    def __init__(self,number,suit) -> None:
        self.number = number
        self.suit = suit
        
class Player(Card):
    pass
    
    
