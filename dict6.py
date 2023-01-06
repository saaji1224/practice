#Ways to sort list of dictionaries by values in Python – Using itemgetter
# Sort the values using sorted()
# Sort the keys alphabetically using for loop and sorted() function
# Sort the values alphabetically using lambda functions

dic= {1: 13, 2: 7, 3: 0, 4: 10 } # define a dictionary

sorted_dic= {}   # declear another empty dictionary
sorted_keys = sorted(dic, key=dic.get)    ##

print("Original dictionary: ",dic)
print("Sorted dictionary: ", sorted_dic)
for i in sorted_keys:
    sorted_dic[i] = dic[i]

print(sorted_dic)


# sorting based on values

dic= {'A': 11, 'B': 20, 'C': 10, 'D': 6 }

print("Original dictionary: ",dic)

sorted_list = sorted(dic.items(), key=lambda j:j[1])

sorted_dic= {key:val for key, val in sorted_list}

print("Sorted dicitonary: ")
print(sorted_dic)