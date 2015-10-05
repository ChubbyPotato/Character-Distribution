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

lc=n.lower()

#l=str(list(string.ascii_lowercase))
potato=str(lc.count(l))

for x in potato:
    a=string.count('a')
    b=string.count('b')
    c=string.count('c')
    d=string.count('d')
    e=string.count('e')
    f=string.count('f')
    g=string.count('g')
    h=string.count('h')
    i=string.count('i')
    j=string.count('j')
    k=string.count('k')
    l=string.count('l')
    m=string.count('m')
    n=string.count('n')
    o=string.count('o')
    p=string.count('p')
    q=string.count('q')
    r=string.count('a')
    s=string.count('a')
    t=string.count('a')
    u=string.count('a')
    v=string.count('a')
    w=string.count('a')
    x=string.count('a')
    y=string.count('a')
    z=string.count('a')