"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    """Description of the method here"""    
    return list([number, number+1, number+2])

def concatenate_rounds(rounds_1, rounds_2):
    """
    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    return list( rounds_1 + rounds_2 )
def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """
    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.
    
    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    """Description of the method here"""
    approx_average1 = (hand[0]+hand[-1]) / 2
    approx_average2 = hand[len(hand)//2]
    return card_average(hand) in {approx_average1, approx_average2}
        
def average_even_is_average_odd(hand):
    """Description of the method here"""
    odd_list = hand[::2]
    even_list = hand[1::2]
    return card_average(odd_list) == card_average(even_list)

def maybe_double_last(hand):
    """Description of the method here"""
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
