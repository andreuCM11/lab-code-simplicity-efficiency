"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import string

#with the string library we avoid having to type all the characters
def RandomStringGenerator(l=12,a=list(string.ascii_letters + string.digits)):
#we eliminate the p char and replace the while loop by using a range in a for
    s = ''
    for _ in range(l):
        s += random.choice(a)
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for _ in range(n):
        #we eliminate this line because we have and esle statement that already aborts when needed
        if a < b:
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))
