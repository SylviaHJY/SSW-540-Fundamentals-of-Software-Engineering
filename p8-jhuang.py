#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p8-jhuang.py
@Time    :   2022/10/31 01:29:54
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   Create a Python program that prompts the user for the name of a file with an arbitrary ASCII document, reads the file, and prints a summary of the words in the document.
'''
# First download files from website and name the files
import urllib.request 
import os
urllib.request.urlretrieve("http://www.py4inf.com/code/mbox.txt", "mbox.txt");
urllib.request.urlretrieve("http://www.py4inf.com/code/mbox-short.txt", "mbox-short.txt");


#import string
import string
string.punctuation

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

else:
   d = dict();
   for line in fhand:
    line = line.rstrip();
    line = line.replace('—','!');
    line = line.translate(line.maketrans('','',string.punctuation));
    line = line.lower();
    words = line.split();
    for word in words:
      d[word] = d.get(word,0) + 1; 
      '{:,}'.format(d[word]);
     

   
   sum = 0;
   characterList = dict();
   for key in d:
    for i in key:
      if(i.isalpha()):
       characterList[i] = characterList.get(i,0) + d[key]; 
    sum = sum + d[key];
   

   #print(distinctWords);
   print('There are total:','{:,}'.format(sum),' words.');
   print('There are total:', '{:,}'.format(len(d)),' distinct words.');

   #convert direction to list
   l1 = list(d.items());
   #Sort in descending order, using reverse=True
   l1.sort(key=lambda x: x[1], reverse = True)
   l2 = l1[:25];
   #l1.sort(d.items(),key = itemgetter(1),reverse=True);
   print('The top 25 most frequent words and counts are: ', l2);

   characterListSort = list(characterList.items());
   characterListSort.sort(key=lambda x: x[1], reverse = True);
   for i in range(len(characterListSort)):
    print(characterListSort[i][0],',', end =" ");

