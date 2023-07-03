import numpy as np

def suits(cards_objs):
    return [card.suit for card in cards_objs]

def numbers(card_objs):
    return [card.number for card in card_objs]

def is_sequence(numbers):
    temp_numbers=np.sort(numbers)
    return len(set(np.diff(temp_numbers)))==1

def is_same_suit(suits):
    return len(set(suits))==1

def is_same_number(numbers):
    return len(set(numbers))==1

def highest_card_is_ace(numbers):
    temp_numbers = np.sort(numbers)
    return temp_numbers[0]==1