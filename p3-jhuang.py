#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p3-jhuang.py
@Time    :   2022/09/26 00:42:33
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   define a function called 'maxOfThree' that takes three values 
             and returns the maximum value of the three
'''

while True:
  try:
    first_Int = int(input('Enter first value:'))
    break
  except:
    print('Please enter int number only')
    continue

while True:
  try:
    second_Int = int(input('Enter second value:'))
    break
  except:
    print('Please enter int number only')
    continue

while True:
  try:
    third_Int = int(input('Enter third value:'))
    break
  except:
    print('Please enter int number only')
    continue

# find the maximum of three
def Max_of_three(input1,input2,input3):
# declare an empty array to store users input
  array = [input1,input2,input3]
  maximum = array[0]
  for i in range(len(array)):
    if(array[i] > maximum):
      maximum = array[i]
  return maximum

print(f'The maximum of {first_Int} {second_Int} {third_Int} is {Max_of_three(first_Int,second_Int,third_Int)}')
