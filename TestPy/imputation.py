'''
Created on 30 Mar 2015

@author: yvonne
'''

from pandas import *
import numpy

 # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']
    
baseball = pandas.read_csv("/home/yvonne/Downloads/lahman-csv_2015-01-24/Master.csv")
baseball['weight']=baseball['weight'].fillna(numpy.mean(baseball['weight']))
print(baseball['weight'])