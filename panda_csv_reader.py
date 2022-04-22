#!/usr/bin/env python3
import pandas as pd


#Enter 0-1000, None, or leave blank
col_width = 100 
col_input= input('Set Column width (0-1000 or none): ')

#
if col_input in range(1000):
        col_width = int(col_input)
        
elif col_input == ['None','none', '']:
	col_width = None
else:
	Exception('You entered the wrong value!!!!(0-1000 or None')

#Set dataframe to show all rows requested
#set column width for longer or shorter text
pd.set_option('display.max_rows', None)
pd.options.display.max_colwidth = col_width

#Enter entire path
file = input("Enter filepath to view: ")
rows = int(input("Enter number of rows to view: "))

#commands to create dataframe 

#reads files with specified delimiter for csv formatted files

df = pd.read_csv(file, encoding = "utf-16", delimiter=",")
#prints out specified number of rows from top to bottom
print(df.head(rows))

