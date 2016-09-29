# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:28:52 2016

@author: Xinying
"""
#question1-3#
import pandas as pd #import panda firstly from the panda package
data=pd.read_table('/Users/Xinying/Desktop/iris.data.txt',header=0,sep = ',')
#Also can use the text editor to add the names of columns, named 0 with the first row,
#and use ','to separate the columns 
print(data)# display the data
#question4#
data.head(n=10)#read the first 10 rows data
data.tail(n=10) #read the last 10 rows data
#question5#
data.describe().transpose()#get the simple statistis
#question6#
data.hist()#print the histogram for each of the columns 
data.classone.value_counts().plot(kind='bar')#plot the bar chart for each column
