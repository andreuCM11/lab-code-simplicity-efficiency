"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
#intead of looking for all the possible triangles and then choosing the max, 
#we start looking from high to low and we keep the first we find
def my_function(a):
    for x in reversed(range(5,a)):
        for y in reversed(range(4,a)):
            for z in reversed(range(3,a)):
                if (x*x==y*y+z*z):
                    return max([x, y, z])
    return 0

a = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(a))))

