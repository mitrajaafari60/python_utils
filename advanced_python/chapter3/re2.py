import re
str = 'This is an advanced Python programming in Maktabkhooneh.'
result = re.sub(r'maktabkhooneh','university',str)
print(result)