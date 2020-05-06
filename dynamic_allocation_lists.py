#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Author: Bipin P. (mailto: bipinp2013@gmail.com)
http://iambipin.com
101010101    10  101010101    10  101     10    101010101
1010101010   10  1010101010   10  1010    10    1010101010
10      101  10  10      101  10  10 01   10    10      101
10      101  10  10      101  10  10  10  10    10      101
1010101010   10  1010101010   10  10   01 10    1010101010
1010101010   10  101010101    10  10    1010    101010101
10      101  10  10           10  10     010    10
10      101  10  10           10  10      10    10
1010101010   10  10           10  10      10    10
101010101    10  10           10  10      10    10  10
Python Program that converts a floating point decimal number to binary number
"""
list_main = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
folds = int(input('Enter the no. of folds: ').rstrip())
section = int(len(list_main)/folds)
start_index = 0
end_index = 0
counter = 1

for i in range(folds):
    if counter == 1:
        end_index += section
        globals()['list{0}' .format(i)] = list_main[start_index:end_index]
        counter += 1
    elif counter == folds:
        globals()['list{0}' .format(i)] = list_main[end_index: ]
        counter += 1
    elif counter < folds:
        start_index = end_index
        end_index += section
        globals()['list{0}' .format(i)] = list_main[start_index:end_index]
        counter += 1

for i in range(folds):
    print('List {0}: {1}' .format(i, globals()['list{0}' .format(i)]))

