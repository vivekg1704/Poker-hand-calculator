from misc import is_same_suit, is_sequence, highest_card_is_ace
import numpy as np

def hands(cards):
    numbers_array = np.array([card.number for card in cards])
    suits_array = np.array([card.suit for card in cards])

    print(cards)
    print(np.array([(card.suit,card.number) for card in cards]))

    if is_sequence(numbers_array):
        if is_same_suit(suits_array):
            if highest_card_is_ace(numbers_array):
                return 'ROYAL FLUSH'
            return 'STRAIGHT FLUSH'
        return 'STRAIGHT'
    else:
        if is_same_suit(np.array([card.suit for card in cards])):
            return "FLUSH"
        elif len(set(numbers_array))==2:
            if np.any([i==4 for i in np.unique(numbers_array,return_counts=True)[1]]):
                return 'FOUR OF A KIND'
            if np.any([i==3 for i in np.unique(numbers_array,return_counts=True)[1]]):
                return 'FULL HOUSE'
        elif len(set(numbers_array))==3:
            if np.any([i==3 for i in np.unique(numbers_array,return_counts=True)[1]]):
                return 'THREE OF A KIND'
            else:
                return 'TWO PAIR'
        elif len(set(numbers_array))==4:
            return 'PAIR'
        else:
            return 'HIGH CARD'
        
        

    





