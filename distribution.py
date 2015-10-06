"""
distribution.py
Author: Suhan Gui
Credit: Stack Overflow

Assignment: Character Distribution

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

string=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "{0}" is:'.format(n))

from collections import Counter
import string

def count_letters(word, valid_letters=string.ascii_letters):
    count = Counter(word) # this counts all the letters, including invalid ones
    return sum(count[letter] for letter in valid_letters) # add up valid letters

word = "The grey old fox is an idiot"
print(count_letters(word))