#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   p4-jhuang.py
@Time    :   2022/09/29 23:38:54
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :  write a script (a program) that implements a “Guess the Number” game.
'''

import random


name = input('Hello!What is your name?')
print('Well,' + name + ' I am thinking of a number between 1 and 20.');

# get a random number between 1 and 20
guessNumber = random.randint(1,20)

def checkResult(num1, num2):
  if(num1 == num2):
    return 0;
  elif(num1 < num2):
    return -1;
  elif(num1 > num2):
    return 1;

i = 0;
while(i < 6):
  guess = input("Take a guess:")
  try:
    guess = int(guess);
    try:
      if(guess <= 0 or guess > 20):
        raise ValueError()
    except ValueError:
      print('Oops. The number is between 1 and 20. Try again!')
      continue;
  except:
    print("Only integers are allowed");
    continue

  i += 1;
  ans = checkResult(guess,guessNumber);
  if(ans == 0):
    print('Good Job,' + name + '! You guessed my number in ' +  str(i) + ' guesses!');
    break;

  elif(ans == -1):
    print('Your guess is too low.');
    continue;

  elif(ans == 1):
    print('Your guess is too high.')
    continue;

if(i == 6):
  print('The number I was thinking of was ' + str(guessNumber));


  
    



    

