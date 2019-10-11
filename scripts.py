# CHARIF Mahdi
import numpy as np


# PROBLEM 1




# Exercise 1 - Say "Hello, World!" Python

print ("Hello, World!")



# Exercise 2 - Python If - Else

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())


if n%2!=0:
    print("Weird")
elif (n%2==0 and n>=2 and n<=5):
    print("Not Weird")
elif (n%2==0 and n>=6 and n<=20):
    print("Weird")
elif (n%2==0 and n>20):
    print("Not Weird")


# Exercise 3 - Arithmetic operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)


# Exercise 4 - Loops

if __name__ == '__main__':
    n = int(input())

if n>=1 and n<=20:
    for i in range(n):
        print(i**2)

#I have put a condition on n to know whether the number is contained between 1 and 20. If so, we print the square of each number until n-1.



# Exercise 5 - Write a function

def is_leap(year):
    leap = False

    # I begin with the most complex condition, that includes the biggest amount of conditions. Otherwise, if I had put the year%4==0 condition alone first, it would have given us some false results
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

# Exercise 6 - Print function

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())

s=0
for nb in range(1, n+1):
    print (nb, end="")



# Exercise 7 - Capitalize!


def solve(s):
    if len(s)>0 and len(s)<1000:
        l = s.split(" ")
        final = l[0].capitalize()
        #I put the first world, with a brand new capital letter, as the first letter of my new string. If there is no other word found, we don't enter in the loop.
        if len(l)>1:
            for i in range(1,len(l)):
                final = final + " " + l[i].capitalize()
    return(final)


# Exercise 8 - Python : division

from __future__ import division

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)



# Exercise 9 - Print Function

if __name__ == '__main__':
    n = int(input())

s=0
for nb in range(1, n+1):
    print (nb, end="")



# Exercise 10 - List comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    L =[] # This list is intended to store the good combinations
    
    for num1 in range(x+1):

        for num2 in range(y+1):

            for num3 in range(z+1):
                if num1 + num2 + num3 != n:
                    L.append([num1,num2,num3])
    print(L)
                
#I must verify that the sum of the three integers put in each list is different from n




# Exercise 11 - Find the runner-up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

newlist = list(arr)
z = max(newlist)
while max(newlist) == z:
    newlist.remove(max(newlist))

print (max(newlist))



# Exercise 12 - Nested lists

n = int(input())
marksarray = []
sco = [] # I will store all the scores inside this list
for _ in range(n):
    student = input()
    score = float(input())
    marksarray.append([student, score])
    sco.append(score)
secondelement = sorted(set(sco))[1] # I get the second element of the set, which is the second lowest grade 

for student,mark in sorted(marksarray) :
    if mark == secondelement :
        print(student)



# Exercise 13 - Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
list = student_marks[query_name] #I create a list of the marks of the chosen student
print("{0:.2f}".format(sum(list)/len(list))) #I use "{0:.2f}" to keep two digits of precision
# I thought about print(round(sum/len),2) but it does not work here

# Exercise 14 - Map and lambda function

cube = lambda x : x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    L=[0,1] #I initialize the list with the first two fibonacci numbers
    for k in range(2,n):
        L.append(L[k-2]+L[k-1]) #I use the usual formula given by the recursive form
    return(L[0:n])
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# Exercise 15 - Lists

n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd == 'print':
        print(l)
    elif cmd == 'insert' and len(args)==2:
        l.insert(int(args[0]),int(args[1]))
    elif cmd == 'append' and len(args)==1:
        l.append(int(args[0]))
    elif cmd == 'remove' and len(args)==1:
        l.remove(int(args[0]))
    elif cmd == 'pop':
        l.pop()
    elif cmd == 'reverse':
        l.reverse()
    elif cmd == 'sort':
        l.sort()



# Exercise 16 - Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
tup = tuple(integer_list)
print(hash(tup))
#The last step is the one which converts the tuple I created to a hash type



# Exercise 17 - sWAP cASE

def swap_case(s):
    final = ''
    for let in s:
        if (let.islower()) : # I check if the chosen letter is a lowercase one and, if so, I pass it to an uppercase letter
            final+=let.upper()
        elif (let.isupper()) : # I check if the chosen letter is an uppercase one and, if so, I pass it to a lowercase letter
            final+=let.lower()
        else : # If there is anything else than a letter, I put back the same character
            final+=let
    return(final)

# Exercise 18 - String split and join

def split_and_join(line):
    # write your code here
    a = line.split(" ") #We separe the words or other characters contained in line
    return("-".join(a))


# Exercise 19 - What's your name

def print_full_name(a, b):
    print("Hello " + a + " " + b +"! " + "You just delved into python.")

# Exercise 20 - Mutations

def mutate_string(string, position, character):
    l=[]
    final = ''
    for k in range(len(s)):
        l.append(s[k]) # We create a list of all the characters of the given string
    l[position] = character # We change the character in the right position
    for i in range(len(l)):
        final += l[i]
    return(final)


# Exercise 21 - Find a string

def count_substring(string, sub_string):
    c1=0
    c2=0
    for k in range(len(string)-len(sub_string) + 1):
        if string[k] == sub_string[0] :
            c1 = 1
            # I give this item the value one to compare it when I leave the loop to know whether I found the same sub string in the general string
            for i in range(len(sub_string)):
                if string[k+i]!=sub_string[i] :
                    c1=0
                    break
            if c1 == 1:
                c2+=1 #I add one to the total of times the sub string appears
    return(c2)



# Exercise 22 - String validator

if __name__ == '__main__':
    s = input()
alphanum = False
alphabet = False
digit = False
lower = False # I simply create a boolean for each type and check if the string verifies them.
upper = False
for k in s :
    if k.isalnum() :
        alphanum = True
    if k.isalpha() :
        alphabet = True
    if k.isdigit() :
        digit = True
    if k.islower() :
        lower = True
    if k.isupper() :
        upper = True
print(alphanum)
print(alphabet)
print(digit)
print(lower)
print(upper)


# Exercise 23 - Text alignment

#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# Exercise 24 - Text wrap


def wrap(string, max_width):
    s = 0
    L = []
    f = ''
    while (s+max_width)<len(string):
        L.append(string[s:s+max_width])
        s+= max_width
    L.append(string[s:len(string)])
    for i in range(len(L)):
        f+=L[i]+"\n" #I get back the items of the list, which contains the new strings with a length equal to max_width. I add "\n" to go back to the line
    return(f)



# Exercise 25  - Designer door mat


#I begin with the upper part of the pattern :
N, M = map(int,input().split())
for k in range(1,N,2): 
    print((k * ".|.").center(M, "-")) #This is the upper pattern. If I proceeded by incrementing i by 1 until N, I would get 4 unwanted.|.
print("WELCOME".center(M,"-")) 
for k in range(N-2,-1,-2): 
    print((k * ".|.").center(M, "-"))  # This is the lower pattern



# Exercise 26 - String formatting

def print_formatted(number):
    # your code goes here
    wid = len(str(bin(number)).replace('0b',''))
    f = ''
    for num in range(1, number+1):
        dec = str(num)
        octo = str(oct(num)).replace('0o','')
        hexa = str(hex(num)).replace('0x','').upper() #I replace the lowercase letters by their uppercase equivalent
        bina = str(bin(num)).replace('0b','')
        print(dec.rjust(wid), end=' ')
        print(octo.rjust(wid), end=' ')
        print(hexa.rjust(wid), end=' ') 
        print(bina.rjust(wid)) #By using the rjust method, I can print the 4 formats of the number with a space between them equivalent to the width equal to the number
    return()

# Exercise 27 - Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    lowercase = list('abcdefghijklmnopqrstuvwxyz') # I gather all the lowercase letters
    low = lowercase[0:size]
    for k in range(size-1, -size, -1):
        numb = abs(k)
        alph = low[size:numb:-1]+low[numb:size]
        print ("--"*numb+ '-'.join(alph)+"--"*numb)


# Exercise 28 - The minion game

def minion_game(string):
    # your code goes here
    
#I create a string which contains all the vowels accepted

    allvowels = 'AEIOU'
    scores = 0
    scorek = 0

    for i in range(len(string)):
        if string[i] in allvowels:
            scorek += (len(string)-i)
        else:
            scores += (len(string)-i)

    if (scorek > scores) :
        print ("Kevin", scorek)
    elif (scorek < scores) :
        print ("Stuart", scores)
    else:
        print ("Draw")
    return()



# Exercise 29 - Merge the tools !

def merge_the_tools(string, k):
# your code goes here
    while string:
        s = string[0:k]
        f = '' # We create a new string to add in it a block of letters
        for char in s:
            if char not in f : # If we don't find the same character in f, we add it to f so that we get a non existing block
                f += char
        print(f) # We print the obtained block of characters and go back to the loop
        string = string[k:]



# Exercise 30 - Introduction to sets

def average(array):
    # your code goes here
    L = []
    for k in array :
        if k not in L :
            L.append(k)
    return(sum(L)/len(L))


# Exercise 31 - Symmetric difference

M = int(input())
i1 = input()
N = int(input())
i2 = input()
L = [] # This list will be used to store the distinct items
L2=[]
L3 = []
L1 = i1.split(" ")

for k in range(len(L1)):
    L2.append(int(L1[k]))
L1 = i2.split(" ")
for k in range(len(L1)):
    L3.append(int(L1[k])) # I fill these two lists to have both values of M and N

L = list(set(L2).difference(set(L3))) + list(set(L3).difference(set(L2))) # I only keep the distinct elements between the lists

final = sorted(L)
for u in range(len(L)) :
    print(final[u])


# Exercise 32 - No idea !

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

array = input().split()

A = set(input().split())
B = set(input().split()) # I insert the two sets of m integers

final = sum([(number in A) - (number in B) for number in array])

print(final)


# Exercise 33 - Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input()) #Number of countries input
L = []
L1 = []
for k in range(n) :
    new = input()
    L.append(new)
for x in L :
    if x not in L1:
        L1.append(x)

print(len(L1))


# Exercise 34 - Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split())) #This is the set
numb = int(input()) # This is the number of operations that will be done

for _ in range(numb):
    ins = input().split()
    cmd = ins[0]
    if len(ins)>1:
        args = int(ins[1])
    if cmd == 'discard':
        s.discard(args)
    elif cmd == 'remove' and args in s :
        s.remove(args)
    elif cmd == 'pop':
        s.pop()
print(sum(s))



# Exercise 35 - Set intersection

# Enter your code here. Read input from STDIN. Print output to STDOUT

fr = int(input())
lfr = set(map(int,input().split()))
en = int(input())
lengl = set(map(int,input().split())) # I create the two sets of students

print(len(lfr.intersection(lengl))) # I print the number of similar elements


# Exercise 36 - Set union

# Enter your code here. Read input from STDIN. Print output to STDOUT

fr = int(input())
lfr = set(map(int,input().split()))
en = int(input())
lengl = set(map(int,input().split())) # I create the two sets of students

print(len(lfr.union(lengl)))


# Exercise 37 - Set difference

# Enter your code here. Read input from STDIN. Print output to STDOUT

fr = int(input())
lfr = set(map(int,input().split()))
en = int(input())
lengl = set(map(int,input().split())) # I create the two sets of students

print(len(lfr.difference(lengl)))


# Exercise 38 - Set symmetric difference

# Enter your code here. Read input from STDIN. Print output to STDOUT

fr = int(input())
lfr = set(map(int,input().split()))
en = int(input())
lengl = set(map(int,input().split())) # I create the two sets of students

print(len(lfr.symmetric_difference(lengl)))


# Exercise 39 - Set mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())
set1 = set(map(int, input().split())) # This is the set we consider as an input
n = int(input())

for _ in range(n): # I am using _ because I do not need to use a variable to be iterated in this loop
    cmd, _ = input().split()
    set2 = set(map(int, input().split()))
    if(cmd == "intersection_update"): # I consider the 4 different situations : if we write intersection_update, update, symmetric_difference_update or difference_update)
        set1.intersection_update(set2)
    elif(cmd == "update"):
        set1.update(set2)
    elif(cmd == "symmetric_difference_update"):
        set1.symmetric_difference_update(set2)
    elif(cmd == "difference_update"):
        set1.difference_update(set2)

print(sum(set1))


# Exercise 40 - The captain's room

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
a = input()
l = list(map(int,a.split()))
r = set(map(int,a.split())) # I will compare the total of times each item of the set
# appears in the list and conclude who the captain is
for item in r:
    l.remove(item)
    if item not in l: # If I cannot find the item, it means that it was found in l and removed
        print(item)
        break


# Exercise 41 - Check subset

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input()) #This is the number of tests

for _ in range(n):
    nb1 = int(input()) # Number of items of A
    A = set(input().split()) # Creation of set A
    nb2 = int(input()) # Number of items of B
    B = set(input().split()) # Creation of set B
    print(A.issubset(B)) # This simple line prints out a boolean which will be true if A is actually a subset of B


# Exercise 42 - Check strict superset

# Enter your code here. Read input from STDIN. Print output to STDOUT


#I use the all method to check if all the items of strictsuperset
a = set(map(str, input().split(' ')))
n = int(input())
strictsuperset = []
for _ in range(n): # I will not use the variable of the loop so I prefer to use _
    newset = set(map(str, input().split(' ')))
    strictsuperset.append(a.issuperset(newset))
if all(strictsuperset):
    print("True")
else:
    print("False") # I print the result : True or False


# Exercise 43 - Collections counter

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = list(map(int,input().split())) # These two first lines are the number of shoe sizes and the list of the sizes
nb = int(input()) # This is the number of orders
L = [] # This list (which will become a matrix) will store all the orders
s = 0

for k in range(nb):
    a = list(map(int,input().split())) # I do not put split(" ") because split() gives us the same result
    if a[0] in l : # If the asked size is not available, we don't add the potential gain to the sum
        s += a[1]
        l.remove(a[0]) # Each time an element of "a" is in the list of the sizes,
        # I remove the size from the list. This is important in particular when the list of sizes contains the same size multiple times
print(s) # I print the sum of all the gains


# Exercise 44 - Defaultdict tutorial

from collections import defaultdict

d = defaultdict(list)
n, m = list(map(int, input().split()))
L = []  # This list will store the indexes of the values of B found in A
for k in range(n):
    a = input()
    d['A'].append(a)
for i in range(m):
    b = input()
    d['B'].append(b)  # I create the defaultdict and create its two keys

for u in range(m):

    if d['B'][u] in d['A']:  # I check if each element of B is in A. If so, I recover the index in A of this element
        L.append([i for i, x in enumerate(d['A']) if x == d['B'][u]])  
        # I append to L the indexes of the elements of B (there could be multiple indexes so I use enumerate in a loop to get all of them

    else:
        L.append([-1])  # If the value is not found in A, I cannot recover an index so I append to L the value -1

for j in range(len(L)):

    if L[j] != [-1]:

        for k in range(len(L[j]) - 1):  # I print the indexes of each value of B in A on the same line but keep the last index for the end,
            # so that I can get stay on the same line for each range of indexes
            print(str(L[j][k] + 1), end=" ")
        print(str(L[j][len(L[j]) - 1] + 1))

    else:
        print(str(L[j][0]))  # If a value of B is not in A, I print -1


# Exercise 45 - Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input()) # We enter the number of operations we will do

for k in range(n):
    a, b = list(input().split())
    try:
        print (int(a)//int(b)) # If none of the two exceptions are met, I print the integer division of a and b
    except ValueError as Error : # If a is divided by 0, we do not do the division but print an error
        print ("Error Code:",Error)
    except ZeroDivisionError as Error : # If there is an error on the type of the variables (not integers), we print an error
        print ("Error Code:", Error)



# Exercise 46 - Collections namedtuple

# Enter your code here. Read input from STDIN. Print output to STDOUT

# In order to keep my work understandable and readable, I prefer to write this problem in more than 4 lines

from collections import namedtuple

allmarks = [] # This
n = int(input())
columns = input().split() # We enter the names of the columns, no matter the order they are put in

GeneralStudentTuple = namedtuple('GeneralStudentTuple', columns) # I create a tuple which contains all the columns we have entered. It will enable me get the column "Grade" from it

for k in range(n) : # I could also have written for _ in range(n) as I do not use k in my loop
    L = input().split()
    # I now want to make a new instance in GeneralStudentTuple : as a matter of fact, I want to add the marks from all the information like the id etc...

    allmarks.append(int(GeneralStudentTuple._make(L).MARKS)) #  I only recovered the marks and get them all together in a list

# The final step is to calculate the average : let us just sum all the items in the list which contains the marks and divide it by the length of the list

print(round(sum(allmarks) / len(allmarks), 2))


# Exercise 47 - Collections orderedDict

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

fooddict = OrderedDict()  # I first create my ordered dictionary

n = int(input()) # Number of orders
L1 = [] # In each loop, this loop will contain the name of the product
L2 = [] # This one will contain the amount of money

for _ in range(n):
    L = input().split()
    a = int(L[len(L) - 1]) # I store the price of the product to be able to add it to the total gain due to the sales of this same product

    if " ".join(L[:-1]) not in fooddict : # If the key does not exist, we create it
        fooddict[" ".join(L[:-1])] = int(L[len(L) - 1])
    else :
        fooddict[" ".join(L[:-1])] = fooddict[" ".join(L[:-1])] + int(L[len(L) - 1])
        # I get back the name of the product and the price
        # SEPARATELY and store it in the dictionary

for product in fooddict:
        print(product + " " + str(fooddict[product])) # I print the name of the product and the money it has brought


# Exercise 48 - Word order

from collections import OrderedDict

n = int(input())
L= [] # This list will contain all the words
dictwords = OrderedDict() # This dictionary will contain the word and its number of occurrences

for k in range(n):
    word = input()
    if word not in dictwords : # If the word is not amongst the keys of the dictionary, I add it to the dictionary
        dictwords[word] = 1
    else : # If it is already in it, I just iterate the number of occurrences
        dictwords[word] += 1
print(len(dictwords)) # I print the detected number of distinct words
for k in dictwords :
    print(str(dictwords[k]) + " ",end='') # I print the number of occurrences of each word
# (in the order in which they had been introduced, that is why I used an ordered dictionary).


# Exercise 49  - Collections deque

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

n = int(input())  # I enter the number of operations that will be made later
d = deque()

for _ in range(n):
    L = input().split()
    if L[0] == 'append': # If the operation asked is append or appendleft, I will have two elements in L.
        # If pop or popleft is asked, there is no other parameter to take into consideration.
        d.append(L[1])
    if L[0] == 'appendleft':
        d.appendleft(L[1])
    if L[0] == 'pop':
        d.pop()
    if L[0] == 'popleft':
        d.popleft()
for k in range(len(d)): # I print each element of d, which is a deque. It will give us its final elements.
    print(str(d[k]) + " ", end='')


# Exercise 50 - Piling up!

n = int(input())

# For this program, I have thought about splitting the given list into two parts. Indeed, if we want
# all the cubes to be put on each other successively, we can simply locate the minimum of the list and check if the lists composed
# of all the elements on its left and all the elements on its right are sorted. If so, we can print Yes !

for _ in range(n):
    nb = int(input()) # Number of items in the considered test case
    L = list(map(int,input().split())) # This list contains each set of values representing the length of the cubes
    minimum = min(L)
    indmin = L.index(minimum) # I get the index of the minimum of the list
    # I can now create the two lists : the one of all the elements on the right of the minimum,
    Lright = L[indmin + 1:]
    Lleft = L[:indmin] # This one contains all the items on the right of the minimum

    # Let us these two lists are sorted (in a decreasing way for the left list).

    leftsort = sorted(Lleft, reverse = True)
    rightsort = sorted(Lright)

    if Lleft == leftsort and Lright == rightsort :
        print("Yes")
    else :
        print("No")
    # If Lright and Lleft were originally sorted, it means that we can compile the cubes.


# Exercise 51 - Company logo

from collections import Counter # I will use this subclass : https://docs.python.org/2/library/collections.html

if __name__ == '__main__':
    s = input()

listcounter = Counter(s).items() # This dictionary contains all the characters. An important point is that

sortedlistcounter = sorted(listcounter, key=lambda x: (-x[1], x[0])) # The -x[1] enables me to sort by decreasing numbers
# The second key of this sorting enables me to sort the characters in an alphabetical order if they have the same number of occurrences

if len(sortedlistcounter)>=3: # I distinguish the cases where there are less than three characters to print from the other cases
    for k in range(3):
        print(sortedlistcounter[k][0] + " " + str(sortedlistcounter[k][1]))
else :
    for i in range(len(sortedlistcounter)):
        print(sortedlistcounter[i][0] + " " + str(sortedlistcounter[i][1])) # Less than 3 characters and their occurrences will be printed out


# Exercise 52 - Time delta

from datetime import datetime

nbofdates = int(input())
typeofdate = '%a %d %b %Y %H:%M:%S %z'
#the format is defined to be introduced in the strptime function of the datetime library.
# cf : https://www.tutorialspoint.com/python/time_strptime.htm
for _ in range(nbofdates):
    time1 = input()
    time2 = input()
    difference = datetime.strptime(time1, typeofdate) - datetime.strptime(time2, typeofdate)
    print(int(abs(difference.total_seconds())))
    # total_seconds enables me to get the difference between the two dates in seconds
#We use the absolute function to avoid having a negative difference between the two
# times we consider


# Exercise 53 - Calendar module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime


def dayoftheweek(date):
    splitdate = date.split(" ")
    d = datetime.date(int(splitdate[2]), int(splitdate[0]), int(splitdate[1]))
    # The first is the year, the second the month and the third the day

    return (d.strftime("%A").upper())
    # The strftime method gives the weekday name when we specify %A in its parameters


print(dayoftheweek(input()))

# Exercise 54 - Zipped

import itertools as it

n, x = list(map(int,input().split()))
L =[] # This list will become a matrix and will contain all the marks
for _ in range (x):
    a = list(map(float,input().split()))
    L.append(a)

marks = list(it.zip_longest(*L, fillvalue= None)) # zip_longest enables to use the zip function for a quite long list

# I can now print the average mark of each student :
for i in range(len(marks)):
    print(sum(marks[i])/len(marks[i])) # I simply print the division between the sum of the marks of each student and
    #the number of marks he got


# Exercise 55 - ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = list(input())
# Each of the following lists are intended to store the characters of a precise type :
up = [] # Uppercase letters
low = [] # Lowercase letters
odd = [] # Odd numbers
eve = [] # Even numbers


for item in s: # I append to all the lists the values or characters that go within.
    if item.isupper():
        up.append(item)
    if item.islower():
        low.append(item)
    if item.isdigit() : # Since I cannot use int(item) in the condition, I prefer to directly use a built-in function
        if int(item)%2!=0 :
            odd.append(int(item))
        else :
            eve.append(int(item))
final = sorted(low) + sorted(up) + sorted(odd) + sorted(eve) # I can now concatenate all these lists after having sorted them

for k in range(len(final)):
    print(str(final[k]),end='') # I use the parameter 'end' in order to print all the sorted characters next to each others


# Exercise 56 - Athlete sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

sortedlist = sorted(arr, key = lambda x : x[k]) # I sort the array regarding k

# I distinguish the cases when m = 1 from the others so that I can use a loop

for k in range(n): # Lastly, I want to print all the characteristics of an athlete on the same line
    if m > 1:
        for i in range(m-1):
            print(sortedlist[k][i], end=' ') # I print all the items of an athlete on the same line
        print(sortedlist[k][m-1]) # I print the last one out of the loop so that I can go back to a new line after this one
    else:
        print(sortedlist[k][0])


# Exercise 57 - Detect floating point number

# Enter your code here. Read input from STDIN. Print output to STDOUT

from re import match, compile  # As we are in the regex part, I will use its tools.

# I used this website to learn how to use regex : http://www.pyregex.com/

n = int(input())
L = []  # This list will contain the boolean which will point out if each input is a floating point number

c = compile(
    '^[-+]?'  # Matches + or - AT THE BEGINNING OF the string WITH JUST 0 or 1                           sign (just + or - or nothing)
    '[0-9]*'  # Matches any number
    '\.' 
    '[0-9]+$')  # There must be one or more digits at the end of the input (for instance, we cannot just write '+' without a single digit after it

for _ in range(n):
    L.append(bool(c.match(
        input())))  # Once a character matches with one of the                                                 characteristical patterns of a floating string                                           number, we print True

# I could have printed the result in this loop but I prefer to do it in the next one, in order to be clear on my program

for k in range(len(L)):
    print(L[k])  # I print the booleans that tell whether or not the input respects the                     conditions

# Exercise 58 - Re.split()

regex_pattern = r"[.,]"	# Do not delete 'r'.
# I specify . and , as items to be deleted from the output


# Exercise 59 - Group(), Groups() and Groupdict()

import re

Repet = re.search(r'([a-zA-Z0-9])\1', input().strip())
# The hooks are used to contain the letters (uppercase and lowercase) and the numbers
# the \1 helps us to match only when a character occurs multiple times

if Repet :
    print(Repet.group(1)) # I only pick up the first item of Repet because I want the first character to have been repeated on the set
else :
    print(-1)


# Exercise 60 - Re.findall() and Re.finditer()

import re
vow = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz' # I will use these two strings in the parameters of re.findall
stringex = input() # We enter the string we need as an input


Repet = re.findall(r'(?<=[' + cons + '])([' + vow + ']{2,})[' + cons + ']', stringex, re.IGNORECASE)
# I am instructing the program to find two or more vowels between consonants (you can see that the group ([' + vow + ']{2,}) is put between two groups of consonants
# [' + vow + ']{2,} is used to instruct that we are looking for 2 or more vowels.

# We use Ignorecase in order to consider an uppercase and a lowercase as the same, for instance

if Repet:
    for k in range(len(Repet)):
        print(Repet[k]) # I print all the matched substrings on different lines thanks to "*" and "\n".
else:
    print('-1')
    

# Exercise 61 - Re.start() and Re.end()

import re

stringex = input()  # We enter the string we want to analyze
pattern = input()  # This is the pattern we want to figure out if it is in the input string

m = re.compile(r"(?=("+pattern+"))") # I use ?= to compile if and only if I find the pattern

findpattern = m.search(stringex)  # I am looking for one or more occurrences of this pattern in stringex

if findpattern:  # This condition means that we execute what is inside it if a match is found

    for match in m.finditer(stringex):  # I print all the matches that are found thanks to the iterator finditer
        print((match.start(1), match.end(1) - 1))
        # We print a tuple containing the start and end of each match. I remove 1 from the second index because match.end(1) goes one index too far from what we want

else:
    print((-1, -1))


# Exercise 62 - Regex substitution

import re

n = int(input())
L = []  # This list will store all the new modified lines

for _ in range(n):
    line = input()  # I enter each line separately
    newline = re.sub(r" \&\&(?= )", " and", line)
    newline = re.sub(r" \|\|(?= )", " or",
                     newline)  # I put (?=) because I want to catch the && sign if and only if there is a space after it. For instance, it would make no sense to transform "||||||" to "orororor"

    # Also, I will not modify the || and && that are put between quotation marks
    L.append(newline)

for k in range(len(L)):
    print(L[k])  # I print all the modified lines


# Exercise 63 - Validating Roman Numerals

regex_pattern = r"^M{,3}(CM|CD|C|D?C{,3})(XC|XL|X|L?X{,3})(IX|IV|I|V?I{,3})$"

# The pattern should begin with the highest power of 10 possible (here, we can accept until 10^3 which corresponds to M)
# I put the question mark to make every roman digit optional : I could simply have X without any other roman digit like I or C
# The hooks are intended to specify the number of times the same roman character can occur. For instance, concerning M, we can just put it three times in a row as it equals 1000 and we can only go until 3999




# Exercise 64 - Validating phone numbers


import re
n = int(input()) # This is the number of phone numbers to check and I do not need to convert it into a list of integers

pattern = r"^[789][0-9]{9}$"

# I wrote this in order to verify that the number begins with 7, 8 or 9.
# After having verified that, I must verify that there are 9 other digits to complete the number (10 digits in total)

for _ in range(n) :
    number = input()
    if (bool(re.match(pattern, number))): # If the number respects all the condition, I can print YES. Otherwise, NO will be printed
        print("YES")
    else :
        print("NO")


# Exercise 65 - Validating and parsing Email Addresses

import email.utils
import re

n = int(input()) # Number of mails to test
patternmail = r'^[A-Za-z][\w._-]+@[A-Za-z]+\.[a-zA-Z]{1,3}$'
# This is the structure of a valid e-mail. It MUST finish with letters, after having put a dot
# I have used the + symbol to say that I can put the character multiple times. For instance, I can put as many letters or digits as I want before the @ symbol

for _ in range(n):
    userandmail = input()
    tup = email.utils.parseaddr(userandmail) # This tuple contains, separetely the name of the user and his e-mail
    if re.search(patternmail, tup[1], re.I):
        print(userandmail)


# Exercise 66 - Hex Color Code

import re

n = int(input()) # Number of lines
pattern = r'[\s:.(](#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})[\s;,)]' 
# {3,6} means that we want colors of 3 or 6 letters (between a to f, A to F ) or/and digits.
# It MUST begin with a hashtag (thanks to "^")
# [\s:.(] enables me to precise all the characters that can be put
# ahead of the hashtag, which are a blank space (\s) and all the other characters I have written
# Similarly,[\s;,)] is about the end
# I put this condition in order not to print #BED and #CAB, like in the test case given on hackerrank

for _ in range(n):
    line = input()
    goodcolors = re.findall(pattern, line)
    if  goodcolors:# This list contains all the valid colors
        for colors in goodcolors:
            print(colors) # I directly print all the correct colors




# Exercise 67 - HTML Parser - Part 1

from html.parser import HTMLParser


# I begin by using the class given above and modify the functions to adapt to our problem


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for k in range(len(attrs)):
            print('->', attrs[k][0], ">", attrs[k][1])  # I recover the name AND the value

    def handle_endtag(self,
                      tag):  # If the closure of a tag is found, this message must                                      be printed
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for k in range(len(attrs)):
            print('->', attrs[k][0], ">", attrs[k][1])  # I recover the name AND the value                                                         from attrs


n = int(input())  # Number of lines
parser = MyHTMLParser()

for _ in range(n):
    parser.feed(input())

# Exercise 68 - HTML Parser Part 2

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        # I have to handle the case where the data is a line break (\n)
        if data != '\n':
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        # To be able to handle the case in which the data is made of comments on several         lines, I will split data
        if '\n' not in data:
            print(">>> Single-line Comment")
        else:
            print(">>> Multi-line Comment")
        print(
            data)  # I simply print the whole comment, whether it is a multi-line or a                      single-line one


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# Exercise 69  - Detect HTML Tags, Attributes and Attribute Values



from html.parser import HTMLParser

# FOR THIS EXERCISE, I just used the class used in the previous two challenges. I just delete some functions inside it.

# I begin by using the class given above and modify the functions to adapt to our problem


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for k in range(len(attrs)):
            print('->',attrs[k][0],">", attrs[k][1]) # I recover the name AND the value

    def handle_startendtag(self, tag, attrs):
        print (tag)
        for k in range(len(attrs)):
            print('->',attrs[k][0],">", attrs[k][1]) # I recover the name AND the value                                                         from attrs


n = int(input()) # Number of lines
parser = MyHTMLParser()

for _ in range(n):
    parser.feed(input())




# Exercise 70 - Validating UID


import re

T = int(input()) # Number of test cases

pattern = r'^(?=(?:[a-z\d]*[A-Z]){2,})(?=(?:\D*\d){3,})(?:([a-zA-Z\d])(?!.*\1)){10}$'

# [A-Z]){2,} means that there must be at least 2 uppercase letters
# The last group enables us to match exactly 10 characters in a valid UID

for k in range(T):
    string = input()
    if (bool(re.match(pattern, string))) == True:
        print("Valid")
    else :
        print("Invalid")


# Exercise 71 - Validating Credit card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


n = int(input()) # Number of test cases


telnumberpattern = r'^[456][0-9]{3}([-]?[0-9]{4}){3}$' # This pattern represents the first four conditions issued above. As the "-" is not compulsory, I have put a "?" ahead of it to signify that a number can be valid even without it
unallowedpattern = r'(\d)(?:[-]?\1){3,}' # We accept a MAXIMUM of 3 consecutive digts.

for _ in range(n):
    telnumber = input()
    firstcondition = re.match(telnumberpattern,telnumber) # This one is about the first four conditions
    secondcondition = not re.search(unallowedpattern,telnumber) # I want to check if all the forbidden characters are not in my number

    if firstcondition and secondcondition : # If the two conditions are respected, the number is valid
        print("Valid")
    else: # Otherwise, we reject it
        print("Invalid")



# Exercise 72 - Validating Postal Codes

# I will just modify lines 3 and 7 !

regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
# We must check that there are exactly 5 numbers from 1 to 5, so that the input will be contained in [100000,999999]

regex_alternating_repetitive_digit_pair = r"(\d)(?=(\d)\1)"

# I put the lookahead assertion in order to find the match only when the same digit is met again (thanks to \1).



# Exercise 73 - Matrix script

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

unchangedcode = ''.join(matrix[i][j] for j in range(m) for i in range(n))
modifiedcode = re.sub(r'(?<=[0-9a-zA-Z])[\s!@%&#$]+(?=[0-9a-zA-Z])',' ',unchangedcode)
# If there are spaces or symbols between two alphanumeric numbers, I replace them with an empty space, thanks to the sub function of regex

print(modifiedcode)


# Exercise 74 - XML 1 - Find the score


def get_attr_number(node):
    s = 0  # This will be the sum of then number of attributes of each key
    for item in node.iter():
        s += len(item.attrib)  # I get the number of attributes of each element
    return (s)

# Exercise 75 - XML2 - Find the Maximum Depth



maxdepth = 0
def depth(elem, level):
    global maxdepth
    level = level + 1 # As the depth of the root is equal to 0, I add one
    maxdepth = max(maxdepth, level) # I can now compare the biggest depth with the level
    for item in elem:
        depth(item, level)
    # The usefulness of the global variable maxdepth is that I will be able to call it out of the function once I have run the function



# Exercise 76 - Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        numbers = []
        n = len(l)
        for k in range(n):
            numbers.append(l[k][len(l[k])-10:]) # I only get back the 10 LAST digits. Those that come before are either the +91 prefix or just numbers to be left behind
        sortednumbers = sorted(numbers) # I can now sort all the numbers before getting them under the right format

        for k in range (len(sortednumbers)):
            print("+91",sortednumbers[k][:5],sortednumbers[k][5:]) # I can now print the number with the prefix and the right number, divided into two parts at its middle
    return fun



# Exercise 77 - Decorators 2 - Name Directory



def person_lister(f):
    def inner(people):
        # I first need to sort the list of people regarding their age, which is the 3 item of the list
        sortedpeople = sorted(people, key = lambda x : int(x[2])) # The age has a string type, that is why I use a lambda function to get the key of the sorting
        return(map(f, sortedpeople)) # I use the map function by applying the sorting to f, so that I can later get the right format through the use of name_format
    return inner




# Exercise 78 - Arrays



def arrays(arr):
    # complete this function
    # use numpy.array
    reversedlist = [] # I wil luse this list to create the reverses array
    for k in range(len(arr)):
        reversedlist.append(arr[-1-k])
    return(np.array(reversedlist, float)) # I take advantage of the structure of np.array (numpy.array) by specifying the type of the items of the array (float).


# Exercise 79 - Shape and reshape

import numpy as np

numbers = list(map(int, input().split())) # I willuse this list to create the array

print(np.reshape(np.array(numbers),(3,3))) # In a single line, I create the array from the list "numbers", reshape it into a 3x3 array and print the result


# Exercise 80 - Transpose and flatten

import numpy as np

n, m = list(map(int, input().split()))
arr = []  # I initialize the array

for _ in range(n):  # We will enter n lines of numbers
    arr.append(list(map(int, input().split())))  # I append to the array all its new lines

arrtransp = np.transpose(
    arr)  # I can now create and print the transposed and flattened                                matrixes
arrflatten = np.array(
    arr).flatten()  # I convert the array that I appended to a "real"                                        one (with numpy library)

print(arrtransp)
print(arrflatten)

# Exercise 81 - Concatenate

import numpy as np

n,m,p = list(map(int,input().split())) # Number of columns and rows of the two arrays
arrayn = np.empty(shape=(0,0))
arraym = np.empty(shape=(0,0))

arrayn = np.array([list(map(int,input().split())) for _ in range(n)]) # I create the first array, which has n lines
arraym = np.array([list(map(int,input().split())) for _ in range(m)]) # I create the first array, which has m lines
print(np.concatenate((arrayn,arraym), axis = 0))


# Exercise 82 - Zeros and ones

import numpy as np

arg = tuple(map(int,input().split())) # Number of matrixes, lines and columns

print(np.zeros(arg, int), np.ones(arg, int), sep='\n') # I create and print the array composed of zeros and ones



# Exercise 83 - Eye and identity

import numpy as np
# There is a bug in the test cases, I have to add a white space manually
np.set_printoptions(sign=' ')
n, m = list(map(int, input().split()))

print(np.eye(n, m, k = 0))


# Exercise 84 - Array mathematics

import numpy as np

n, m = list(map(int,input().split()))
A = np.array([list(map(int,input().split())) for _ in range(n)], int) # The number of rows depends on the value of n so I introduce a for loop
B = np.array([list(map(int,input().split())) for _ in range(n)], int)

print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))
# I simply do all the operations asked. Numpy provides all the techniques to do so.


# Exercise 85 - Floor, ceil and rint

import numpy as np
# Once again, there is a problem with the white space so I checked on numpy library and I found the following line to introduce at the beginning of the code
np.set_printoptions(legacy = '1.13')


array = np.array(list(map(float, input().split())))
# I can directly print the floor, ceil and rint of this array

print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))


# Exercise 86 - Sum and prod

import numpy as np

n, m = list(map(int, input().split()))

array = np.array([input().split() for _ in range (n)], int) # I create the array
sumarray = np.sum(array, axis = 0)

print(np.prod(sumarray, axis = 0)) # I can directly add these two arrays and print the product of the rows of this new array resulting from the sum of the first and the second



# Exercise 87 - Min and max

import numpy as np
n, m = list(map(int,input().split())) # Dimension of the array

array = np.array([input().split() for _ in range(n)],int)
print(max(np.min(array, axis = 1))) # I can directly get the maximum of the list of minimums by using the function max, with the list of minimums as a paramter alongside the axis.



# Exercise 88 - Mean, var and Std

import numpy as np
# Once again, there is a problem with the output of this program, as it was created with an old version of numpy. To counter this issue, I set the print option of this old version, the 1.13 one
np.set_printoptions(legacy='1.13')
n, m = list(map(int,input().split())) # Dimension of the array

array = np.array([input().split() for _ in range(n)],int)

print(np.mean(array, axis = 1)) # I print the mean along axis 1
print(np.var(array, axis = 0))# I print the  var along axis 0
print(np.std(array, axis = None)) # I print the std along axis None


# Exercise 89 - Dot and cross

import numpy as np
n = int(input()) # The matrix will be a NxN one
# I create the two required arrays considered the input number of lines, n.
A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(n)], int)
print(A.dot(B)) # I just have to use the dot function provided by numpy and print the result of this matrix multiplication.




# Exercise 90 - Inner and outer

import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)
# I input the two arrays
# I just have to use the two functions of numpy that enable me get the inner and outer products

print(np.inner(A,B))
print(np.outer(A,B))


# Exercise 91 - Polynomials

import numpy as np

polynomial = list(map(float,input().split())) # I import the list of the coefficients of the polynomial
x = int(input())
print (np.polyval(polynomial, x)) # I simply apply the polyval method to the list of coefficients, considering the input value of x



# Exercise 92 - Linear algebra

import numpy as np
np.set_printoptions(legacy='1.13') # Once again, I have to introduce this line to bypass the problem of the old version of numpy

n = int(input()) # We have a matrix of dimension nxn

array = np.array([input().split() for _ in range(n)], float) # As we can have float items in the input, I convert each element of the string input to a float type

print (np.linalg.det(array))
# I can now directly print the determinant of the matrix thanks to the linalg.det method








# PROBLEM 2




# Exercise 93 - Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    maximumheight = max(ar)
    count = 0 # I will count the number of items in the array that are equal to the maximum in order to figure out how much candles will be blown out
    for item in ar:
        if item == maximumheight : # If the item is equal to the maximum, I count one more blown candle
            count+=1
    return(count) # I return the number of blown candles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


# Exercise 94 - Kangaroo

# !/bin/python3

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if (v1 > v2):  # If v1<v2, the two kangoroos could NEVER meet at the same time, as x1<x2

        # The problem is quite simple from a mathematical point of view : I have to find the number of jumps such that jump*v1 + x1 = jump*v2 + v2. This equation gives us :
        # jump = (x1 - x2)/(v2 - v1). I can write that because I am inside the condition v1>v2 (so v1!=v2)
        jump = (x1 - x2) / (v2 - v1)

        if jump.is_integer():
            return ("YES")

    return ("NO")  # I return "NO" as x1 and x2 has never been equal AT THE SAME TIME


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Exercise 95 - Viral advertising

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked = [5//2] # I get the numbers of people who liked the content on the first day
    if n == 1 :
        return(liked[0])
    else :
        for k in range(1,n):
            liked.append(liked[k-1]*3//2 )
            # From those who liked the content the day before, three other people per person will be given the content to watch. Only the result of the integer division between this amount of people and 2 will like the ad

    return(sum(liked)) # I return the sum of the likes gathered each day : it will give me the number of likes of the n-th day
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# Exercise 96 - Recursive Digit Sum

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
def superDigit(n, k):
    if len(
            n) == 1:  # If the string n is only composed of 1 item, it means that it is lower than 10 : its super digit is itself
        return (n)
    p = sum([int(item) for item in str(n)])
    p = p * k  # I get the new p, which I temporarily consider as an it. It is equal to its the sum of all its digits multiplied by k (it's stricly the same thing as concatenating p k times)

    return (superDigit(str(p), 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



# Exercise 97 - Insertion sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    L = [] # I will store all the changed arrays in this list
    item = arr[-1] # I store the item I am considering (the last one) to compare it to all the ones that precede it
    i = 2
    while (i < len(arr)+1 and item < arr[-i]): # As I am browsing the array from its end, I use negative indexes
        arr[-i+1] = arr[-i]
        i = i + 1
        print(*arr, sep=" ") # I print all the items for the changed array, separated by                              a white space
    arr[-i+1] = item
    print(*arr, sep=" ") # I print the final version of the array, after having placed arr[len(arr)-1] at its right place
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# Exercise 98 - Insertion Sort - Part 2

# !/bin/python3

import math
import os
import random
import re
import sys


def move(iter, from_, to):
    iter.insert(to, iter.pop(from_))


def insertionSort2(n, arr):
    for k in range(1, n):
        index = k
        # boolean = True # This boolean will be used to figure out if a value at the left         of arr[k] is lower than it
        item = arr[k]  # I store the value I want to compare to all the previous ones
        newarr = arr[:k]  # I create a list of all the items preceding arr[k]

        for a in newarr[
                 ::-1]:  # I browse this list in a reverse way, so that I can keep         the smallest index for which the correspondant item is bigger than arr[k]
            if a >= item:
                index = newarr.index(a)
        move(arr, k,
             index)  # If "index" has not been changed, I will not move the item           as index will be equal to k
        # I am using the move function I have implemented above. It is really convenient         as I can move the other values to the right

        print(*arr,
              sep=" ")  # I can now print all the changed array with their items            separated by white spaces


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)





# END OF THE HOMEWORK CODES



