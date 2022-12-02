'''
@File    :   p5-jhuang.py
@Time    :   2022/10/09 20:43:49
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   use a simplified set of rules for converting singular to plural.
This app is just a really basic one since there are numerous words in the world. We try to include most of them.            
'''

def plural(str):
  
  Mass = ['furniture','information','knowledge','jewelry','homework','marketing','livestock',
'education','courage','bravery','luck','cowardice','greed','clarity','honesty','evidence',
'insurance','butter','love','news','curiosity','satisfaction','work','mud','weather','racism',
'sexism','patriotism','chaos','scenery','help','advice','water','fun','wisdom','silence','sugar',
'coal','spelling','money','moose','sheep','shrimp','water','wine','rice','pasta','coffee','advice',
'luggage','furniture','salt','bread','pork','fruit','flour','cheese','tea','honey','jam','knowledge',
'help','bravery','courage','satisfaction','aggresion','beauty','freedom','faith','grief','guilt',
'humour','accomodation','baggage','travel','traffic','transportation','nature','currency','art',
'poetry','chess','yoga','literature','entertainment','grass','applause','time','air','heat','housework',
'equipment','business','attention','garbage','oil','paper','dirt','dust','land','mud','rain','sunshine',
'mail','music','pajamas','pants','sperm','data','aircraft','analysis','bison','species','swine','series',
'moon','dark','beef','chinese','offspring'];
   
  for i in range(len(str)):
   try:
     if(str[i].isnumeric()):
      raise ValueError();
   except ValueError:
     print('No numbers are accepted.');
     
   else:
    if(str[i].lower() in Mass):
     str[i] = str[i];

    elif(str[i].lower().endswith(('ay','ey','iy','oy','uy'))):
     str[i] = str[i] + 's';

    elif(str[i].lower().endswith(('y'))):
     str[i] = str[i][:-1] + 'ies';

    elif(str[i].lower() == 'photo'):
     str[i] = 'photos';

    elif(str[i].lower().endswith(('o','ch','s','sh','x','z'))):
     str[i] = str[i] + 'es';

    elif(str[i].lower().endswith(('f'))):
     str[i] = str[i][:-1] + 'ves';
  
    elif(str[i].lower() == 'man'):
     str[i] = 'men';
  
    elif(str[i].lower()== 'woman'):
     str[i] = 'women';

    elif(str[i].lower == 'child'):
     str[i] = 'children';

    elif(str[i].lower().endswith(('man'))):
     str[i] = str[i][:-3] + 'men';

    elif(str[i].lower().endswith(('woman'))):
     str[i] = str[i][:-5] + 'women';

    elif(str[i].lower().endswith(('child'))):
     str[i] = str[i][:-5] + 'children';

    elif(str[i].lower() == 'tooth'):
     str[i] = 'teeth';

    elif(str[i].lower() == 'foot'):
     str[i] = 'feet';

    elif(str[i].lower() == 'goose'):
     str[i] = 'geese';

    elif(str[i].lower() == 'half'):
     str[i] = 'halves';

    elif(str[i].lower() == 'mouse'):
     str[i] = 'mice';

    elif(str[i].lower() == 'quiz'):
     str[i] = 'quizzes';

    elif(str[i].lower() == 'wife'):
     str[i] = 'wives';

    else:
     str[i] = str[i] + 's';


arr = input('Please enter:');
arr = arr.strip();
arr = arr.split(" "); # split the string by space into an array
  
plural(arr);

arr1 = " ".join(arr); # join array into string
print(arr1);
