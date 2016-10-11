# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:40:25 2016

@author: Xinying
"""

#Overall Comment: Correct your format according to professor G's format. Once you correct them, I am more than happy to give
#                back your grades. For the content, I think your logic and comments showed your understanding of the code and
#                what you are trying to solve. Good exercise!
###problem 1###
"""
write a function translate()that takes a list of English words and returns 
a list of Swedish words.
"""
def translateword(char):
    translateword = {'merry':'god', 'christmas':'jul', 'and':'och', 'happy':'gott', 'new':
        'nytt', 'year':'ar'} 
    if char in translateword:
        return translateword[char]#if the word is in the key, return to swedish 
    else:
        return char#if the word is not in the key, return to original word

def translate(text):
    l = len(text)#define a variable used to store the length of the string
    translatedtext = [None]*l #creat an empty string
    for i in range(l):#use for loop
        translatedtext[i] = translateword(text[i])#if i in the range string, we
        #get the english word to swedish word
    return translatedtext       

translate(['merry','christmas','and','happy','new','year'])

###problem 2##
"""
Write a function char_freq()that takes a string and builds a frequency listing 
of the characters contained in it.     
"""
def char_freq(text):
    dictionary = {}#creat an empty dictionary
    for i in text:#use for loop
        dictionary[i] = dictionary.get(i,0) + 1 #if i is in the 
        #dictionary, add 1 to i
    return dictionary#if i is not in the dictionary, return to 0 to i

char_freq('abbabcbdbabdbdbabababcbcbab')

###problem 3###
"""
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read the following secret message: 
Pnrfne pvcure? V zhpu cersre
Pnrfne fnynq!
"""
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}   
def rot_13(code):   
    newcode=''   # creat an empty string
    for char in code:   # use for loop
        if char in key:   # if the letter is inthe key list
            newcode+=key[char]   # then we decode the letter to newcode
        else:#if the letter is not in the key list
            newcode+=char   # then keep the character
    return newcode

rot_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')        

###Problem 4###
"""
Define a simple "spelling correction" function correct()that takes a s
tring and sees to it that 1) two or more occurrences of the space
character is compressed into one, and 2) inserts an extra space after a 
period if the period is directly followed by a letter.
"""
def correct(string):
     import re #import regular string
     correction = re.sub(' +',' ',string) #remove extra spaces
     finalcorrection = re.sub('\.','. ',correction)#put extra space after period
     print(finalcorrection) #get final correct string
   
correct("This  is    very funny and cool.Indeed!")
         
###problem 5###
"""
The third person singular verb form in English is distinguished by the 
suffix -s, which is added to the stem of the infinitive form: run -> runs.
"""
def make_3sg_form(word):
    newWord = ''#creat an empty string
    if word.endswith('y'): # if the verb ends in y
        newWord = word[:-1]+'ies' # remove it and add ies
    elif word.endswith('o'): # if the verb ends in o
        newWord = word + 'es' # add es
    elif word.endswith('ch'): # if the verb ends in ch
        newWord = word + 'es' # add es
    elif word.endswith('s'): # if the verb ends in s
        newWord = word + 'es' # add es
    elif word.endswith('sh'): # if the verb ends in sh
        newWord = word + 'es' # add es
    elif word.endswith('x'): # if the verb ends in x
        newWord = word + 'es' # add es
    elif word.endswith('z'): # if the verb ends in z
        newWord = word + 'es' # add es
    else: # all other endings
        newWord = word + 's' # add s
    return newWord 
    
make_3sg_form('try')
make_3sg_form('brush')
make_3sg_form('run')
make_3sg_form('fix')

###problem 7###
"""
Using the higher order function reduce(), write a function max_in_list()that 
takes a list of numbers and returns the largest one. 
"""
def max_in_list(lst):
    largest=0 #initialize largest   
    for i in lst: #use for loop 
        if i>=largest:#compare i with the new largest number
            largest=i  #if i >= largest, then we get i is the new largest number
    return largest#if i<largest, then return this number to new largest

max_in_list([1,2,3,4,5,6])

###problem 8###
"""
Write a program that maps a list of words into a list of integers representing 
the lengths of the correponding words.
"""
def map_list(words):
    lengths = []#creat an ampty list
    for word in words:#use for loop
        lengths. append(len(word))#map the list of words into a list of integers
        return lengths#return to a new length

map_list(['app','mathematics','no'])


def map_list(words):#input a list of strings           
    return list(map(len,words))#output a list of integers
    
map_list(['app','mathematics','no'])


def map_list(words):
    l= len(words)#initianlize l 
    listints=[len(words[i])for i in range(l)]# using the len function to length
    #the current word
    return listints
    
map_list(['app','mathematics','no'])
    

###problem 9
"""
Write a function find_longest_word()that takes a list of words and returns
the length of the longest one. Use only higher order functions.
"""
def find_longest_word(a_string):
    return max(list(map(len,a_string)))#using the above len() to map the list 
    #of words into a list of integers, then using the max() function to find 
    #greatest number

find_longest_word(['math', 'statistics', 'world'])


###problem 10###
"""
Using the higher order function filter(), define a function 
filter_long_words()that takes a list of words and an integer nand returns the 
list of words that are longer than n. 
"""
def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))#using the given length n 
    #to filter the words that the length is longer than n. then we return the 
    #list of those words

filter_long_words(['math', 'what is','mathematics'], 5)

###problem 11### 
"""
 Use the higher order function map()to write a function translate() that 
 takes a list of English words and returns a list of Swedish words. 
"""
def translate(words):
    dict = {'merry':'god', 'christmas':'jul', 'and':'och', 'happy':'gott',
           'new':'nytt', 'year':'år'}#setting a list that what english words 
           #can be translated to swedish
    return list(map(lambda x: dict[x.lower()], words))#map the english words to 
    #swedish, if the english word no corresponding swedish, return to original 
    #word
    
 
translate(['merry','christmas','and','happy','new','year'])


###problem 12###
"""
Implement the higher order functions map(), filter()and reduce().
"""
def map(function,list):
    newlist=[]#creat an empty new list
    for i in list:#use for loop
        newlist.append(function(i))#using function(i) to the new list
        return newlist #get a newlist

map(lambda x: 1+x,[1,2,3,4,5])

def filter(function,list):
    newlist = []#creat an empty new list
    for i in list:#use for loop
        if function(i) == True: #the item whether is true
            newlist.append(i) #if it is true, then using to newlist
    return newlist
    
filter(lambda x:x>3,[1,2,3,4,5,6])

def reduce(function,list):
    accum=list[0]#initialize the accum 
    for i in list[1:]:#use for loop, every i starts from the second place in list
        accum = function(accum,i)#using function with accume and i
    return accum

reduce(max,[1,2,3,4,5,6])



