#Handling missing keys in Python dictionaries
#get() method
dic= {'IND': 'India', 'USA': 'United States of America', 'AUS': 'Australia' }
# key is present
print(dic.get('USA','Not Found'))
#key is not present
print(dic.get('PAK','Not found'))

#setdefault() 
dic= {'IND': 'India', 'USA': 'United States of America', 'AUS': 'Australia' }
# default val
dic.setdefault('JAP', 'Not Found')
# key is present
print(dic['IND'])
#key is not present
print(dic['JAP'])
