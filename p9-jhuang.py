#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p9-jhuang.py
@Time    :   2022/11/07 02:02:29
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   Write a script that finds all of the capitalized words (not words in all caps except individual letters) in a text file and presents them in alphabetical order.
'''

import os
import re
fname = input('Enter the file name: ');
try:
  fhand = open(fname)
  try:
    if(os.stat(fname).st_size == 0 == False):
      raise FileExistsError()
  except FileExistsError:
    print('Empty file.');
    exit();
except:
   print('The file name entered is invalid or does not exist.');
   exit();

#Returns a match where the specified characters are at the beginning or at the end of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")
else:
  result = [];
  for line in fhand:
    line = line.rstrip();
    x = re.findall(r'\b[A-Z][a-z]+|\b[A-Z]\b',line)
    if len(x) > 0:
     result = result + x;
  
  if(len(result) == 0):
    print('Sorry. No capitalized words were found in this file.');
  else:
    result.sort();
    print(result);

