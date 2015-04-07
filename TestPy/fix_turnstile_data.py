'''
Created on 30 Mar 2015

@author: yvonne
'''
#def fix_turnstile_data(filenames):
import csv
'''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
filenames = 'turnstile_110528.txt'
#create file input
f_in = open(filenames,'r')
#create file output
f_out = open('updated_'+filenames,'w')

#create csv reader
reader_in = csv.reader(f_in,delimiter=',')

#create csv writer 
writer_out = csv.writer(f_out,delimiter=',')

for line in reader_in :
    type_record = [line[0],line[1], line[2]] 
    #print(type_record)
    
    for x in xrange(len(line)):
        print('the value of modular' + str((len(line)-2)/5))
        i=8
        l=0
        for j in range((len(line)-2)/5):
            
            l=i+5
            print('the value of l' + str(l))
            if(j==0):
                line_1 = line[3:8]
                line_2 = type_record [0],type_record[1],type_record[2],line_1[0],line_1[1],line_1[2], line_1[3],line_1[4]
            else:
                line_1 = line[i:l]
                line_2 = type_record [0],type_record[1],type_record[2],line_1[0],line_1[1],line_1[2], line_1[3],line_1[4]
                i=l
            print('the value of i'+ str(i))
        
        
        
        
        
           
            
            writer_out.writerow(line_2)    
f_in.close()
f_out.close()       