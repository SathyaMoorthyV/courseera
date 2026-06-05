"""Functions to help edit essay homework using string manipulation."""
def capitalize_title(title):
    """Description of the method here"""
    return title.title()
    
def check_sentence_ending(sentence):    
    """Description of the method here"""
    return sentence.endswith('.')

def clean_up_spacing(sentence):
    """Description of the method here"""
    return sentence.strip()
    
def replace_word_choice(sentence, old_word, new_word):
    """Description of the method here"""   
    return sentence.replace(old_word, new_word)
