EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 20
      
def bake_time_remaining( time ):
    """Preparation time in minutes 
        This function module call is to calculate the preparation
        Preparation time in minutes"""
    elapsed_bake_time = EXPECTED_BAKE_TIME - time
    return elapsed_bake_time

def preparation_time_in_minutes( number_of_layers ):
    """Preparation time in minutes 
        This function module call is to calculate the preparation
        Preparation time in minutes"""
    return number_of_layers * 2

def elapsed_time_in_minutes( number_of_layers , elapsed_time_in_minutes ):
    """Preparation time in minutes 
        This function module call is to calculate the preparation
        Preparation time in minutes"""
    return ( number_of_layers * 2 ) + elapsed_time_in_minutes

