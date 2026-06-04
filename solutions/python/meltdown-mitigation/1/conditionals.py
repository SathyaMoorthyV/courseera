"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and ( temperature * neutrons_emitted < 500000 ):
        return True
    return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = ( ( voltage * current ) / theoretical_max_power ) * 100
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    calcualted = temperature * neutrons_produced_per_second
    if calcualted <= ( threshold * 0.9 ):
        return 'LOW'
    elif calcualted >= ( threshold * 0.1 ) and calcualted <= ( threshold * 1.1 ):
        return 'NORMAL'
    return 'DANGER'
        
    
