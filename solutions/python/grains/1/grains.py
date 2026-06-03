def square(number):
    if   number >= 1 and number <= 64:
        return 2 ** ( number - 1)
    else: 
        raise ValueError("square must be between 1 and 64") 
                
def total():
    i = 1
    total = 0
    while i<=64:       
        total = square( i ) + total
        i += 1
    return total
