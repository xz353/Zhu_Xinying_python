# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:40:25 2016

@author: Xinying
"""

"""
5.The third person singular verb form in English is distinguished by the 
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


"""
9.Write a function find_longest_word()that takes a list of words and returns
the length of the longest one. Use only higher order functions.
"""
def find_longest_word(a_string):
    return max(list(map(len,a_string)))#using the above len() to map the list 
    #of words into a list of integers, then using the max() function to find 
    #greatest number

find_longest_word(['math', 'statistics', 'world'])

"""
10.Using the higher order function filter(), define a function 
filter_long_words()that takes a list of words and an integer nand returns the 
list of words that are longer than n. 
"""
def filter_long_words(words, n):
    return list(filter(lambda x: len(x) > n, words))#using the given length n 
    #to filter the words that the length is longer than n. then we return the 
    #list of those words

filter_long_words(['math', 'what is','mathematics'], 5)


