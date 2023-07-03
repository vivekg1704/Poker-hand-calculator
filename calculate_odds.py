from card_file import Card, ALLOWED_CARDS

def calculate(main_player,drawn_cards,number_of_opponents,number_of_sims):

    temp_allowed_cards = ALLOWED_CARDS
    for card_obj in main_player+drawn_cards:
        temp_allowed_cards -= zip(card_obj.number,card_obj.suit)
    
    for player 