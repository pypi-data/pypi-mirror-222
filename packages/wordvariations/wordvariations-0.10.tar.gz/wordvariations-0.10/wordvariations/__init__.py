import os
import string
from functools import lru_cache
from time import time
import random
from ordered_set import OrderedSet
import surroundingkeys
import pandas as pd


def show_all_keyboards():
    surroundingkeys.show_all_keyboards()


@lru_cache
def get_allowed_letters(keyboard_layout, include_numbers=False):
    os.sep.join(surroundingkeys.__file__.split(os.sep)[:-1])
    filepath = (
        os.sep.join(surroundingkeys.__file__.split(os.sep)[:-1])
        + os.sep
        + keyboard_layout
        + ".pkl"
    )
    if not os.path.exists(filepath):
        surroundingkeys.show_all_keyboards()
        raise ValueError("Choose a valid keyboard layout")

    df = pd.read_pickle(filepath)
    allowedletters = "".join(
        df.loc[(df[1].str[:2] == "U+") & df[1].str.contains("LETTER", na=False)][1]
        .str[2:6]
        .apply(lambda x: eval(r'"\u' + x + '"'))
        .to_list()
    )
    allowedletters = allowedletters.lower() + allowedletters.upper()
    if include_numbers:
        allowedletters = allowedletters + string.digits
    return allowedletters


def switch_letters(
    text: str,
    keyboard_layout: str,
    max_switches: int = 2,
    switch_numbers: bool = False,
    timeout: int | float = 0.3,
) ->list:
    """
    Generate variations of the input text by switching neighboring letters on the specified keyboard layout.

    Parameters:
    -----------
    text : str
        The input text for which to generate variations.
    keyboard_layout : str
        The identifier of the keyboard layout. Should be one of the supported layouts (call show_all_keyboards() to see them).
    max_switches : int, optional
        The maximum number of switches to perform. Default is 2.
    switch_numbers : bool, optional
        If True, allows switching numbers as well. Default is False.
    timeout : int or float, optional
        The maximum time (in seconds) to spend generating variations. Default is 0.3 seconds.

    Returns:
    --------
    list
        A list containing the original text (index 0) and the variations obtained by switching neighboring letters.
        The variations may include up to `max_switches` switches, and the result is unique, preserving the order.

    Example:
    --------
    from wordvariations import switch_letters, change_letters, show_all_keyboards
    text = "Gustavo Lima"
    keyboard_layout = "kbdbr_1"
    print(
        switch_letters(
            text=text,
            keyboard_layout=keyboard_layout,
            max_switches=10,
            switch_numbers=False,
            timeout=0.3,
        )
    )
    ['Gustavo Lima', 'Gutsavo Lima', 'Gutsavo Lmia', 'Gutsaov Lmia']

    Note:
    -----
    The function uses an LRU cache to speed up repeated calls with the same inputs.
    """

    allowedletters = get_allowed_letters(
        keyboard_layout, include_numbers=switch_numbers
    )
    switchesdone = set()
    allresults = OrderedSet()
    allresults.add(text)
    timeout = time() + timeout

    while len(allresults) <= max_switches:
        if time() > timeout:
            break
        try:
            while True:
                if time() > timeout:
                    raise TimeoutError
                g = random.randint(1, len(text) - 2)
                if g in switchesdone:
                    continue
                if (
                    (text[g] not in allowedletters)
                    or (text[g + 1] not in allowedletters)
                    or (text[g - 1] not in allowedletters)
                ):
                    continue
                text = text[:g] + text[g + 1] + text[g] + text[g + 2 :]
                switchesdone.add(g)
                switchesdone.add(g + 1)
                switchesdone.add(g - 1)
                allresults.add(text)
                break

        except Exception:
            break

    return list(allresults)


@lru_cache
def index_all(l, n):
    l = list(l)
    indototal = 0
    allindex = []
    while True:
        try:
            indno = l[indototal:].index(n)
            indototal += indno + 1
            allindex.append(indototal - 1)
        except ValueError:
            break
    return allindex


def change_letters(
    text: str, keyboard_layout: str, max_change: int = 1, include_numbers: bool = False
) -> str:
    r"""
    Generate variations of the input text by changing some of the letters to their neighboring keys on the specified keyboard layout.

    Parameters:
    -----------
    text : str
        The input text for which to generate variations.
    keyboard_layout : str
        The identifier of the keyboard layout. Should be one of the supported layouts (call show_all_keyboards() to see them).
    max_change : int, optional
        The maximum number of letters to change. Default is 1.
    include_numbers : bool, optional
        If True, includes numbers in the allowed letters. Default is False.

    Returns:
    --------
    str
        A variation of the input text with some letters changed to neighboring keys.

    Example:
    --------
    from wordvariations import switch_letters, change_letters, show_all_keyboards
    text = "Gustavo Lima"
    keyboard_layout = "kbdbr_1"
    for q in range(3):
        print(change_letters(text, keyboard_layout, max_change=1, include_numbers=False))
    # Gustavo Limq
    # Gjstavo Lima
    # Vustavo Lima

    Note:
    -----
    The function uses an LRU cache to speed up repeated calls with the same inputs.
    """

    allreadydone = set()
    textlistoriginal = list(text)
    textlist = list(text)
    random.shuffle(textlist)
    allowedletters = list(
        get_allowed_letters(keyboard_layout, include_numbers=include_numbers)
    )
    for letter in textlist:
        try:
            result = surroundingkeys.get_next_letters(
                letter=letter, keyboard=keyboard_layout
            )
            allletters = list(
                set(
                    result[letter]["side"]
                    + result[letter]["top"]
                    + result[letter]["bottom"]
                )
                & set(allowedletters)
            )
            indiall = index_all(tuple(textlistoriginal), letter)
            random.shuffle(indiall)
            for indi in indiall:
                if indi in allreadydone:
                    continue

                textlistoriginal[indi] = random.choice(allletters)
                allreadydone.add(indi)
                break
            if len(allreadydone) >= max_change:
                break
        except Exception:
            continue
    return "".join(textlistoriginal)
