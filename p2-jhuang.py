while True:
  try:
    score = float(input('Please enter your score:'))   
  except:
    print('Please enter a number.')
    continue

  if score > 100.0 or score < 0.0:
    print('Invalid inputs, your score range is between 0 and 100.')
  
  elif 92.0 < score and score <= 100.0:
    print('Your grade is A')

  elif 90.0 <= score and score <= 92.0:
    print('Your grade is A-')

  elif 87.0 <= score and score <= 89.9:
    print('Your grade is B+')
  
  elif 83.0 <= score and score <= 86.9:
    print('Your grade is B')

  elif 80.0 <= score and score <= 82.9:
    print('Your grade is B-')

  elif 70.0 <= score and score <= 79.9:
    print('Your grade is C')

  else:
    print('Your grade is F')

  choose = input('Do you want to exit? (Y/N):')
  if choose.lower() == 'y':
     break
  elif choose.lower() == 'n':
    continue
  else:
    print('Invalid input, please reenter:')
    choose = input('Do you want to exit? (Y/N):')
    if choose.lower() == 'y':
      break;
    elif choose.lower() == 'n':
      continue
    else:
      print('OK!BYE~~')
      break

 

  
    



  