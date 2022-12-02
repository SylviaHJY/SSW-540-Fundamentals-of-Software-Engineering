#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p7-jhuang.py
@Time    :   2022/10/24 12:29:45
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   find the number of unique senders and the email address and number of emails sent by the address that sent the most email messages.
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

else:
  d = dict();
  for line in fhand:
    if not line.startswith('From: '):
      continue
    emails = line.split();
    d[emails[1]] = d.get(emails[1],0) + 1;
  
  #print(d);
  lst = list(d.keys());
  print('There are:',len(lst),' unique sender email addresses');

  Max_email_numbers = 0;
  Max_email_numbers_Sender = "";
  for key in d:
    if (d[key] > Max_email_numbers):
      Max_email_numbers = d[key];
      Max_email_numbers_Sender = key;
  print('User: ',Max_email_numbers_Sender,'sent the most email messages, total: ',Max_email_numbers);


  # Way2:
  #lst = list(d.keys());
  #print('There are:',len(lst),' unique sender email addresses');
  #convert direction to list
  #l1 = list(d.items());
  #print(l1);
  #Sort in descending order, using reverse=True
  #l1.sort(key=lambda x: x[1], reverse=True);
  #print(l1);
  #print('User: ',l1[0][0], 'sent the most email messages, total: ',l1[0][1]);
