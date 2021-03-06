'''
Created on 25 Mar 2015

@author: yvonne
'''

import numpy
from pandas import DataFrame, Series


'''
Using the dataframe's apply method, create a new Series called 
avg_medal_count that indicates the average number of gold, silver,
and bronze medals earned amongst countries who earned at 
least one medal of any kind at the 2014 Sochi olympics.
    
You do not need to call the function in your code when running it in the
 browser - the grader will do that automatically when you submit or test it.
'''

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']
gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
olympic_medal_counts = {'country_name':countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}    
df = DataFrame(olympic_medal_counts)
    
    # YOUR CODE HERE
# one_medal = df[['bronze','gold','silver']]
# 
# df1 = one_medal[(one_medal.gold >= 1) | (one_medal.bronze >= 1) | (one_medal.silver >= 1)]
# avg_bronze = numpy.mean(df1.bronze)
# avg_gold = numpy.mean(df1.gold)
# avg_silver = numpy.mean(df1.silver)
# avg_medal_count = Series([numpy.mean(df1.gold),numpy.mean(df1.silver),numpy.mean(df1.bronze)],index=['gold','silver','bronze'])

avg_medal_count = df[['gold','silver','bronze']].apply(numpy.mean)


print(avg_medal_count)
