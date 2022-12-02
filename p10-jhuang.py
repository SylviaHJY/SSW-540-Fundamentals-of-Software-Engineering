#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p10-jhuang.py
@Time    :   2022/11/14 12:35:40
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   Collected the summary data, plot the data in a bar chart of MatPlotLib 
             change interpreter "command + shift + p" to python3.9.12('base') to run this file.
'''

import matplotlib.pyplot as plt
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

else:
  days = dict();
  #months = dict();
  #years = dict();
  for line in fhand:
    if not line.startswith('From '):
      continue
    info = line.split();
    days[info[2]] = days.get(info[2],0) + 1;
    #months[info[3]] = months.get(info[3],0) + 1;

  name_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  num_list = [days['Sun'],days['Mon'],days['Tue'],days['Wed'],days['Thu'],days['Fri'],days['Sat']];
  plt.bar(range(len(num_list)),num_list,tick_label = name_list);
  plt.show();

  #name_list = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  #num_list = [months['Jan'],];
  #plt.bar(range(len(num_list)),num_list,tick_label = name_list);
  #plt.show();
  

 
  
  

  

