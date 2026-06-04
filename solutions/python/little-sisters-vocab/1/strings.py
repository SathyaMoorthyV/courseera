"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    result = [ vocab_words[0] ]
    for i in range( len(vocab_words) ):         
           if    i != 0:
                result.append( vocab_words[0] + vocab_words[i] ) 
    return ' :: '.join(result)

def replace_i_with_y(iword):
    return iword[:len(iword)-1] + 'y'
    
def remove_suffix_ness(word):
    withoutness = word[:len(word)-4]
    if withoutness[-1:] == 'i':
        withoutness = replace_i_with_y( withoutness)
    return withoutness 
    
def adjective_to_verb(sentence, index):
    
    Adjective = sentence.split()[index]
    if Adjective[-1:] == '.':
       Adjective = Adjective[:len(Adjective)-1]
    return Adjective + 'en'
