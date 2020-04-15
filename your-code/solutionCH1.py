"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

def convert_str_int(x):
    if x.lower()=='zero':
        return 0
    if x.lower()=='one':
        return 1
    if x.lower()=='two':
        return 2
    if x.lower()=='three':
        return 3
    if x.lower()=='four':
        return 4
    if x.lower()=='five':
        return 5 

def convert_int_str(x):
    sign = ''
    if x <0:
        sign = 'negative '
    x = abs(x)
    if x==0:
       return sign + 'zero'
    if x==1:
       return sign + 'one'
    if x==2:
       return sign + 'two'
    if x==3:
       return sign + 'three'
    if x==4:
       return sign + 'four'
    if x==5:
       return sign + 'five'
    if x==6:
       return sign + 'six'
    if x==7:
       return sign + 'seven'
    if x==8:
       return sign + 'eight'
    if x==9:
       return sign + 'nine'
    if x==10:
       return sign + 'ten'

def plus_minus(a,b,c):
    if b.lower() == ('plus'):
        return (convert_str_int(a) + convert_str_int(c))
    elif b.lower() == ('minus'):
        return (convert_str_int(a) - convert_str_int(c)) 

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')
        
if (not a == 'zero' and not a == 'one' and not a == 'two' and not a == 'three' and not a == 'four' and not a == 'five') or (not c == 'zero' and not c == 'one' and not c == 'two' and not c == 'three' and not c == 'four' and not c == 'five') or (not b == 'plus' and not b == 'minus'):
    print("I am not able to answer this question. Check your input.")  
else:   
    print(a, b, c, 'equals', convert_int_str(plus_minus(a,b,c)))
print("Thanks for using this calculator, goodbye :)")
