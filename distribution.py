"""
distribution.py
Author: Suhan Gui
Credit: Stack Overflow & Nils Kingston

Assignment: Character Distribution

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better):The rain in Spain stays mainly in the plain.
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
from collections import Counter
import string
import operator

word=input("Please enter a string of text (the bigger the better): ")
potato=word.lower()
print('The distribution of characters in "{0}" is:'.format(word))

doge=(dict(map(lambda letter:(letter,len(potato)-len(potato.replace(letter,''))),potato)))
sorted_doge = sorted(doge.items(), key=operator.itemgetter(0))
converted_doge = list(doge.items())

converted_doge.sort(key=lambda f: (-f[1], f[0]))
for x in converted_doge:
    if x[0]!=0 and x[0]!=(" ") and x[0]!=("'") and x[0]!=("$") and x[0]!=("%") and x[0]!=("(") and x[0]!=(")") and x[0]!=(";") and x[0]!=(":") and x[0]!=("!") and x[0]!=(">") and x[0]!=("<") and x[0]!=(",") and x[0]!=("?") and x[0]!=('"') and x[0]!=("="):
        print(x[0]*x[1])