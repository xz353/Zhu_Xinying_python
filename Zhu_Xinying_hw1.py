# -*- coding: utf-8 -*-
"""
@author: xinying zhu
"""
#You grades are influended by your format, please refer to the format that Professor G has shown during the lecture. The content
#we expect between """ are questions you are trying to solve, your input parameters and your output. Once you corrected
#them, I am more than happy to give back your mark!
#Overall Comments: Generally speaking, very good work except some detail mistakes. Good calculation and method ! But please 
# try to comment yourself as detail as possible. For the convenience of other people and also for yourself. I have used
# 'Comment' before all my comments, and you may have a look. If any misunderstanding happen, please email me.
"""
1.Define a function max()that takes two numbers as arguments and returns the 
largest of them.
"""
def print_max(a, b):
    """
    Define a function max()that takes two numbers as arguments and returns the 
    largest of them.
    Parameters: the real numbers
    Return: the larger of two numbers. if they are the same, it returns that number.
    """
    if a > b:
    #the first condition: a is greater than b
        print(a, 'is maximum')
        #print a is maximum
    elif a == b: 
    #else if a equals to b
        print(a, 'is equal to', b)
        #print a is equal to b
    else:
    #the second condition: a is less than b
        print(b, 'is maximum')
        #print b is maximum

        
print_max(17,23)

"""
2.Define a function max_of_three()that takes three numbers as arguments and 
returns the largest of them.
"""
def print_max_of_three(a, b,c):
    """
    Define a function max_of_three()that takes three numbers as arguments.
    Parameters: the real numbers
    Return: the largest of the three numbers. 
    if two or three of the numbers are the same and that number is the largest, it will print that one.
    """
    if a >= b: 
    #compare a and b firstly
        if a >=c:#a is greater or equal to c
           print (a, 'is maximum' ) #print a is maximum 
        else: #a is less than c
            print (c, 'is maximum') #print c is maximum
    else: #compare a <= b
        if b >=c:#b is greater or equal to c
            print (b, 'is maximum')#b is maximum
        else: #b is less than c
            print (c, 'is maximum') #c is maximum


print_max_of_three(3,5,7)
            
"""       
3.Define a function that computes the length of a given list or string.
"""
def length(a):
    """
    Define a function that computes the length of a given list or string.
    Parameters: text, not including spaces
    Return: an integer containing the number of letters of a given list or string
    """
    l = 0 #initialize l
    for x in a:#use for loop
        l = l + 1 #statistic the element number of a
    return l#get the length of a given list or string

length('hello')

"""
4.Write a function that takes a character
"""
def vowel(a):
    """
    Write a function that takes a character
    Parameters: a single character must be entered, otherwise it gives False
    Return: True if a single vowel, false otherwise
    """
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u': 
    #define a variable used to store vowel
        return True#return true
    else: # a is not vowel
        return False#return false

vowel('b')

"""
5.Write a function translate()that will translate a text into "rövarspråket"
"""
def translate(text):
    """
    Write a function translate()that will translate a text into "rövarspråket"
    Parameters: a string
    Return: the initial language translated into the "robber's language" 
    """
    consonants = 'bcdfghjklmnpqrstvwxz' 
    #define a variable used to store final result
    s = ''#create a new empty string
    for i in text:#use for loop
        if i in consonants:#if i is consonants
            s = s + i + 'o' + i #use 'o'to split for consonants
        else: #if i in vowel
            s = s + i #directly output for vowel
    return s#return the translated string

translate('this is fun')    

"""
6.Define a function sum()and a function multiply()that sums and multiplies 
(respectively) all the numbers in a list of numbers.
"""
def sum(n):
    """
    Define a function sum()
    """
    total = 0 #initialize total value
    for number in n: #use for loop
        total = total + number#add each number to next number,one by one to total
    return total#get a new total, then return to total
#Comment: it would be better to say you add numbers one by one to total
sum([1, 2, 3, 4, 5])

def multiply(m):
    """
    define a function multiply()that sums and multiplies 
    (respectively) all the numbers in a list of numbers.
    """
    total = 1 #initialize total value
    for number in m: #use for loop
        total = total * number# multiply each number to next number
    return total#get a new total, then return to total

multiply([1, 2, 3, 4, 5])

"""
7.Define a function reverse()that computes the reversal of a string.
"""
def reverse(text):
    """
    Define a function reverse()that computes the reversal of a string.
    """
    l = len(text)#initialize l
    a = ''#create a new empty string
    for i in range(len(text)): #use for loop
        a = a + text[l - i - 1] #add the character to a
    return a#return to the reversal of a string
#Comment: It would be better to explain your a = a + text[l-i-1] as using revesal index to get the reversal version of text.
reverse('I am testing')   

"""
8.Define a function is_palindrome()that recognizes palindromes. 
"""
def is_palindrome(word):
    """
    Define a function is_palindrome()that recognizes palindromes. 
    """
    for i in range(0, len(word)): #iterate each i in range, use for loop #Comment: You can simplify as range(len(word))
        if word[i] == word[-(i + 1)]:#if converted string and reversed string
        #are same
            continue #true
        else:
            return False#if converted string and reversed string are not same
    return True#return true

is_palindrome('radar')

"""
9.Write a function is_member()that takes a value (i.e. a number, string, etc) 
xand a list of values a, and returns True if xis a member of a, 
Falseotherwise.
"""
def is_member(a,alist ):#Comment: Why not change the position of the arguments? is_member(a, alist):
    """
    Write a function is_member()that takes a value (i.e. a number, string, etc) 
    xand a list of values a, and returns True if xis a member of a, 
    Falseotherwise.
    """
    for i in a: #use for loop
        if i == alist: #if i equals to a 
            return True#return true
        return False#after a loop, none is equal to i
#Comment: You can improve this function with in. For example: if a in alist: return True
is_member(1,[1,2,3,4])
            
    
"""
10.Define a function overlapping()that takes two lists and returns True 
if they have at least one member in common, False otherwise.
"""
def overlapping(inputlist1, inputlist2):
    """Define a function overlapping()that takes two lists and returns True 
    if they have at least one member in common, False otherwise.
    """
    for i in range(0, len(inputlist1)):#use for loop
        for j in range(0, len(inputlist2)):#use for loop
            if inputlist1[i] == inputlist2[j]:#compare list1 and list2
                return True #two lists have have one pair is same
    return False #two lists have no common member
#Comment: You can improve this function with in, example: for i in inputlist1:
                                                                  #if i in inputlist2 
                                                                  #return True
overlapping(inputlist1 = ['11', '22', '33'], inputlist2 = ['11', '44', '55'])

"""
11.Define a function generate_n_chars()that takes an integer nand a character
cand returns a string, ncharacters long, consisting only of c:s.
"""
def generate_n_chars(numbern, charc):
    """
    Define a function generate_n_chars()that takes an integer nand a character
    cand returns a string, ncharacters long, consisting only of c:s.
    """
    z = ''#create a new empty string
    for i in range(0, numbern):#use for loop
        z = z + charc #repeat n times of the character to new string
    return z #return the new string
    
generate_n_chars(5, 'math')
    
"""
12.Define a procedure histogram()that takes a list of integers and prints 
a histogram to the screen.
"""
def histogram(list):
    """
    Define a procedure histogram()that takes a list of integers and prints 
    a histogram to the screen.
    """
    a = ''#create a new empty string
    for i in list: #use for loop
        a = a + i*'*'+' '#print '*'n times, then get a new string in a 
    return a#get the histogram

histogram([2,4,6])


"""
13.The function max()from exercise 1) and the function max_of_three()from 
exercise 2) will only work for two and three numbers, respectively. 
"""
def max_in_list(list):
    """
    The function max()from exercise 1) and the function max_of_three()from 
    exercise 2) will only work for two and three numbers, respectively. 
    """
    a = list[0] #initialize a
    for i in range(len(list)):#use for loop
        if a <= list[i]:#if a is less or equal to current number in list
            a = list[i]#compare a with the next number i in the list, 
                       #if a <= i, then this number is the new a
        else:#the another condition
            continue#continue compare a 
    return a#return the largest number in the list
    
max_in_list([2,23,31,67,135689,1238521,269,570,2049367,248008084])

"""
14.Write a program that maps a list of words into a list of integers 
representing the lengths of the corresponding words. 
"""
def map_to_lengths_for(words):
    """
    Write a program that maps a list of words into a list of integers 
    representing the lengths of the corresponding words. 
    """
    lengths = [ ]#create an empty list
    for word in words:#use for loop
        lengths. append (len(word))#map the list of words into a list of integers
        return lengths# return to a new length
#Comment: It would be better to explain lengths.append more
map_to_lengths_for(['app','math','world'])

"""
15.Write a function find_longest_word()that takes a list of words and returns 
the length of the longest one. 
"""
def find_longest_word(a_string):
    """
    Write a function find_longest_word()that takes a list of words and returns 
    the length of the longest one. 
    """
    return max(list(map(len,a_string)))#using the above len() to map the list 
    #of words into a list of integers, then using the max() function to find 
    #greatest number

find_longest_word(['math', 'statistics', 'world'])

"""
16.Write a function filter_long_words()that takes a list of words and an 
integer n and returns the list of words that are longer than n.
"""
def filter_long_words(string, number):
    """
    Write a function filter_long_words()that takes a list of words and an 
    integer n and returns the list of words that are longer than n.
    """
    for i in range(len(string)):#use for loop
        listwords=[]#create an empty list
        if len(string[i]) > number:#compare the number of words in list with 
        #the given integer
            listwords.append(string[i])#if the length of the list is not longer
            #than the threshold, then add these words to a new list
    return listwords#return the list of words that are longer than n
    
filter_long_words(['paper', 'note', 'top', 'python','cool'],4)
#Comment: It is not correct to write the listwords=[] within the for loop, because every time you clear up the listwords. So
#        it will only show the result of final input.


    
    
    
    

    
    
