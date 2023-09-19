import re
str = 'students for passing the exam must have more than 15 grade.'
result = re.findall(r'a*',str)
print(result)
print(result)
print(result.count('a'))
print(result.count(''))
print(result.count('a') + result.count(''))