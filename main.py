from card_file import Card
from evaluate_hand import hands
import numpy as np
from calculate_odds import calculate

main_player = [Card(7,'H'),Card(7,'C')]
drawn_cards = [Card(7,'S'), Card(6,'D'), Card (5,'H'),Card (10,'H'),Card (13,'H')]

number_of_opponents = 2

print(calculate(main_player, drawn_cards,100))
3


