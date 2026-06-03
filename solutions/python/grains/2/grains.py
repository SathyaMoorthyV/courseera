def square(number):
    if   number >= 1 and number <= 64:
        return 2 ** ( number - 1)
    raise ValueError("square must be between 1 and 64") 
                
def total():
    counter = 1
    total = 0
    while counter<=64:       
        total = square( counter ) + total
        counter += 1
    return total
