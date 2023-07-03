from card_file import Card
import numpy as np
from evaluate_hand import hands

main_player = [Card(7,'H'),Card(2,'C')]
drawn_cards = [Card(10,'S'), Card(9,'S'), Card (5,'H')]

number_of_opponents = 2

cards = np.array([Card(8,'C'), Card(11,'H'),Card(12,'H'),Card(10,'H'),Card(9,'H')])

print(hands(cards))



