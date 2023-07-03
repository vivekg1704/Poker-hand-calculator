from misc import is_same_suit, is_sequence, highest_card_is_ace
import numpy as np

def hands(cards):
    print(cards)
    print(np.array([(card.suit,card.number) for card in cards]))

    if is_sequence(np.array([card.number for card in cards])):
        if is_same_suit(np.array([card.suit for card in cards])):
            if highest_card_is_ace(np.array([card.number for card in cards])):
                return 'ROYAL FLUSH'
            return 'STRAIGHT FLUSH'
        return 'STRAIGHT'
        
    else:
        if is_same_suit(np.array([card.suit for card in cards])):
            return "FLUSH"





