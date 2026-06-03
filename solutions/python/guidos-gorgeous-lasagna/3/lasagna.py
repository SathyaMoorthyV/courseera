"""Module level text : This gives more context to the code Im writing"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 20
      
def bake_time_remaining( time ):
    """Bake time remaining 
        This function module call returns the 
        bake time remaining """
    elapsed_bake_time = EXPECTED_BAKE_TIME - time
    return elapsed_bake_time

def preparation_time_in_minutes( number_of_layers ):
    """Preparation time in minutes 
        This function module call is to calculate the preparation
        Preparation time in minutes"""
    return number_of_layers * 2

def elapsed_time_in_minutes( number_of_layers , e_time_in_minutes ):
    """Preparation time in minutes 
        This function module call is to calculate the preparation
        Preparation time in minutes"""
    return ( number_of_layers * 2 ) + e_time_in_minutes