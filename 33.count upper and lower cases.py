def count_case_letters(s):
    lower = 0
    upper = 0
    for i in s:
        if i.islower():
            lower += 1
elifi.isupper(): 
            upper += 1
      return upper, lower

string = 'Hello WorlD'
upper, lower = count_case_letters(string)
print('uppercases:', upper)
print('lowercases:', lower)
