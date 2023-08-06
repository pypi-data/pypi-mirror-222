# Generates possible typing errors from a given string (neighboring keys and switch letters) 

## pip install wordvariations 

#### Tested against Windows 10 / Python 3.10 / Anaconda 



## switch_letters: 

This function generates variations by switching neighboring letters in the input text as they might occur due to typographical errors. 
It takes into account the spatial relationships between keys on the specified keyboard layout and creates multiple 
unique variations by switching pairs of neighboring letters.

## change_letters

This function generates variations by changing some of the letters in the input text to neighboring keys on the specified keyboard layout. 
The resulting variations mimic possible errors caused by mistyping or keyboard layout peculiarities. 
Users can control the maximum number of letter changes using the max_change parameter.

These functions are useful for various applications, such as generating typing exercises for language learners, 
creating diverse test datasets for natural language processing applications, or analyzing keyboard layouts' 
ergonomic design. The module's advantages include efficiency through LRU caching, 
customizability with adjustable parameters, and the ability to preserve the order of appearance for unique variations.

Users interested in exploring potential typing errors, keyboard layouts, and text processing applications can 
benefit from this module as it provides an easy-to-use interface for generating diverse text variations based on keyboard layout relationships."



### How to use switch_letters

```python
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
```


### How to use change_letters

```python
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
```