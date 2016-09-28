# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:47:20 2016

@author: Xinying
"""
#question 1-3
import pandas as pd
data=pd.read_csv('/Users/Xinying/Desktop/iris.data.txt')#Also can use the text editor to add the names of columns
#question 4
data.head(10)
data.tail(10)
#question 5
data.describe().transpose()
#question 6
import matplotlib.pyplot as plot
plot.figure('sepal length hist')#creat a new figure
data['sepal length in cm'].hist()#histogram of the data in first column
plot.figure('sepal width hist')
data[' sepal width in cm'].hist()
plot.figure('petal length hist')
data[' petal length in cm'].hist()
plot.figure('petal width hist')
data[' petal width in cm'].hist()

plot.figure('sepal length bar')#creat a new figure
data['sepal length in cm'].plot.bar()#bar plot of the data in first column
plot.figure('sepal width bar')
data[' sepal width in cm'].plot.bar()
plot.figure('petal length bar')
data[' petal length in cm'].plot.bar()
plot.figure('petal width hist')
data[' petal width in cm'].plot.bar()
