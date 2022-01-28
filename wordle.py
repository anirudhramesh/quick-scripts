from functools import reduce
from nltk.corpus import words
import re
import pandas as pd
from operator import and_, or_

# only use lower letters everywhere
_5_letter_words = [w.lower() for w in words.words() if len(w)==5]
exclude_letters = 'adiustowc'
known_positions = {0: 'e'} # dict with format index:letter with index in range(0, 5)
unknown_positions = 'rek'

def use_pandas():
    df = pd.DataFrame(_5_letter_words)[0].str.split('', expand=True).drop([0, 6], axis=1).set_axis(range(5), axis=1)
    df = df[reduce(and_, [~df[col].isin(list(exclude_letters)) for col in df])]
    if known_positions:
        df = df[reduce(and_, [df[pos]==known_positions[pos] for pos in known_positions])]
    df = df[reduce(and_, [reduce(or_, [df[col]==u_letter for col in df]) for u_letter in unknown_positions])]

    filtered = df.agg(''.join, axis=1).values
    return filtered


def use_regex():
    exclude_letters_regex = r'\b[^' + exclude_letters + r']+\b'
    unknown_positions_regex = r'\b(?=.*' + ')(?=.*'.join(unknown_positions) + r').*\b'
    known_positions_regex = ''.join([known_positions[pos] if pos in known_positions else '.' for pos in range(5)])
    
    filtered = []
    for w in _5_letter_words:
        if re.search(exclude_letters_regex, w) and re.search(unknown_positions_regex, w) and re.search(known_positions_regex, w):
            filtered.append(w)
    return filtered


def just_do_it():
    filtered = []
    for w in _5_letter_words:
        if not any(l in exclude_letters for l in w) and all(l in w for l in unknown_positions) and all(w[pos]==known_positions[pos] for pos in known_positions):
            filtered.append(w)

    return filtered


print(use_pandas())
print(just_do_it())
print(use_regex())
