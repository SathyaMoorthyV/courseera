"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    """Short Description"""
    if  card == 'A':
        return 1
    if card in {'K','Q','J'}:
        return 10
    return int(card)

def higher_card(card_one, card_two):
    """Short Description"""
    if  value_of_card( card_one ) > value_of_card( card_two ):
        return card_one
    if value_of_card( card_one ) < value_of_card( card_two ):
        return card_two
    return ( card_one, card_two )

def value_of_ace(card_one, card_two):
    """Short Description"""
    if card_one == 'A' or card_two == 'A':
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Short Description"""
    if    card_one == 'A' or card_two == 'A':
        if value_of_card(card_one) == 10 or value_of_card(card_two) == 10:
            return True    
    return False

def can_split_pairs(card_one, card_two):
    """Short Description"""
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    """Short Description"""
    if value_of_card(card_one) + value_of_card(card_two) in {9,10,11}:
        return True
    return False