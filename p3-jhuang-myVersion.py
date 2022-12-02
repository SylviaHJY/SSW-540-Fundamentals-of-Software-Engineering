#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p3-jhuang.py
@Time    :   2022/09/24 00:53:57
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   requests three values from the user and then prints the maximum of the three values
'''

import re

# Get input from user
first_Value = input('Enter first value:')
second_Value = input('Enter second value:')
third_Value = input('Enter third input:')

# Special Characters considered --> [@_!#$%^&*()<>?/\|}{~:]
# regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 


# check if the input is number
def is_Number(number):
  try:
    float(number)
    return True
  except:
    print(f'{number} is not a number')

# find the maximum of three
def Max_of_three(input1,input2,input3):
# declare an empty array to store users input
  array = [input1,input2,input3]
  maximum = array[0]
  for i in range(len(array)):
    if(array[i] > maximum):
      maximum = array[i]
  return maximum

# decide if three values are same type before compare
# if all the vallues are letters
if first_Value.isalpha() and second_Value.isalpha() and third_Value.isalpha():
  print(f'The maximum of {first_Value} {second_Value} {third_Value} is {Max_of_three(first_Value,second_Value,third_Value)}')

# if all values are numbers
elif is_Number(first_Value) and is_Number(second_Value) and is_Number(third_Value):
  # in case user enter negative numbers, we float() the number before compare
  first_Value = float(first_Value)
  second_Value = float(second_Value)
  third_Value = float(third_Value)
  print(f'The maximum of {first_Value} {second_Value} {third_Value} is {Max_of_three(first_Value,second_Value,third_Value)}')

else:
  print('The type of three inputs should be the same.')

















    
