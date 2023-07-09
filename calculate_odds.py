from card_file import Card
from static_maps_and_constants import ALLOWED_CARDS,HAND_HIERARCHY_MAP
import random
from itertools import combinations
from evaluate_hand import hands
import numpy as np



def calculate(main_player,drawn_cards,number_of_sims):
    counts= {i: 0 for i in HAND_HIERARCHY_MAP}
    cnt=0
    print(number_of_sims)
    temp_allowed_cards = ALLOWED_CARDS
    for card_obj in main_player+drawn_cards:
        temp_allowed_cards.remove((card_obj.number,card_obj.suit))

    for sim in range(number_of_sims):
        for i in range(0,5-len(drawn_cards)):
            number,suit = random.choice(temp_allowed_cards)
            drawn_cards.append(Card(number,suit))
            temp_allowed_cards.remove((number,suit))
        temp_rating = 'HIGH CARD'
        for four_drawn in list(combinations(drawn_cards,4)):
            cards = [main_player[0]]
            cards.extend(four_drawn)
            hand = hands(cards)
            if HAND_HIERARCHY_MAP[hand]<HAND_HIERARCHY_MAP[temp_rating]:
                temp_rating = hand
        for four_drawn in list(combinations(drawn_cards,4)):
            cards = [main_player[1]]
            cards.extend(four_drawn)
            hand = hands(cards)
            if HAND_HIERARCHY_MAP[hand]<HAND_HIERARCHY_MAP[temp_rating]:
                temp_rating = hand
        for three_drawn in list(combinations(drawn_cards,3)):
            cards = main_player
            cards.extend(three_drawn)
            hand = hands(cards)
            if HAND_HIERARCHY_MAP[hand]<HAND_HIERARCHY_MAP[temp_rating]:
                temp_rating = hand
        counts[temp_rating]+=1
    return counts
