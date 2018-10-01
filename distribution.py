"""
distribution.py
Author: Jackson Tolliday
Credit: https://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python, https://docs.python.org/3/tutorial/datastructures.html

Assignment:

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

inp = input(str('Please enter a string of text (the bigger the better): ')).lower()
print('The distribution of characters in "{0}" is:'.format(inp))
ltr = (sorted(list(inp)))       #sort the list
con = ltr.count(' ')
conp = ltr.count('.')
conc = ltr.count(',')
del ltr[0:(con+conp+conc)]      #delete spaces, periods, and commas
ltrlist = []
for x in range(len(ltr)):       #to find where the letters swap in the table
    if ltr[x] != ltr[x+1]:
        y = x+1
        ltrlist.append(y)
    else:
        if ltr[-1] == ltr[x]:
            break

zmax = len(ltr)-1
z=0

for z in range(len(ltr)):      #to delete all letter duplicates
    if z < zmax:
        if ltr[z] == ltr[z+1]:
            del ltr[z]
            ltr.insert(0, 'extra')
        else:
            z = z+1
    else:
        break

for z in range(len(ltr)):      #to delete all letter duplicates
    if z < zmax:
        if ltr[z] == ltr[z+1]:
            del ltr[z]
            ltr.insert(0, 'extra')
        else:
            z = z+1
    else:
        break

for z in range(len(ltr)):      #to delete all letter duplicates
    if z < zmax:
        if ltr[z] == ltr[z+1]:
            del ltr[z]
            ltr.insert(0, 'extra')
        else:
            z = z+1
    else:
        break
exltrcont = ltr.count('extra')

ltrlist.append(len(ltr))

del ltr[0:(exltrcont)]

trultrlist = []
h = 0
for x in range(len(ltrlist)):       #to pin down how many of each letter
    h = ltrlist[x] - ltrlist[x-1]
    trultrlist.append(h)

trultrlist.insert(0, trultrlist[0] + ltrlist[-1])   # to fix 1st variable
del trultrlist[1]

print(trultrlist)

ltrzp = zip(trultrlist, ltr)
ltrzip = sorted(list(ltrzp))
print(ltrzip)

