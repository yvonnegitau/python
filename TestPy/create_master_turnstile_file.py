'''
Created on 30 Mar 2015

@author: yvonne
'''
'''
    Write a function that takes the files in the list filenames, which all have the 
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file. The input files do not have column header
    rows of their own.
    
    For example, if file_1 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    
    and another file, file_2 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 3 ...
    line 4 ...
    line 5 ...
    
    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
output_file = 'output_file.txt'
filenames = 'updated_turnstile_110528.txt'  
with open(output_file, 'w') as master_file:
    master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
    with open(filenames,'r') as reader_in:
        for line in reader_in:
            line  = line.split(",")
            #print(line.split(","))
            master_file.write(line[0]+','+line[1]+','+line[2]+','+line[3]+','+line[4]+','+line[5]+','+line[6]+','+line[7]+'\n')
         
