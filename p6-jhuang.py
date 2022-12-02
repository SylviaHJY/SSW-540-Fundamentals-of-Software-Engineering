#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p6-jhuang.py
@Time    :   2022/10/16 22:02:42
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   Write a program to prompt for a file name, and then read through the file and look for specific lines of the form
'''

# First download files from website and name the files
import urllib.request 
import os
urllib.request.urlretrieve("http://www.py4inf.com/code/mbox.txt", "mbox.txt");
urllib.request.urlretrieve("http://www.py4inf.com/code/mbox-short.txt", "mbox-short.txt");

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
   print('File cannot be opened: ',fname);
   exit();

count = 0;
sum = 0;
for line in fhand:
  line = line.rstrip();
  if(line.find('X-DSPAM-Confidence') == -1):
    continue
  #find the number after -Confidence: position, the index should +1
  confIndex = line.find(':');
  try:
    conf = float(line[confIndex + 1:]) #omit the end
  except:
    print('Bad Value')
    sum = 0;
  else:
    sum = sum + conf;
    count = count + 1;

try:
  average = sum / count
except:
  print('Cannot be divided by 0');
else:
  print('Average spam confidence: ',average);


  
  



