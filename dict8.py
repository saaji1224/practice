#Python program to Merging two Dictionaries
#using ** (double star) operator
#using update() method
# we have used the ** operator to pass all the key-value pairs of both the dictionaries one by one in the new dictionary. 
# This will merge the dictionary, and we can print this result.

dic1= {"name":"sajith","company":"msys","emp":2545 }
dic2= {"technologies":"aws","command":"ls -la"}

dic1.update(dic2)
#merge_dic= {**dic1,**dic2}
d3=dict(zip(dic1,dic2))
print("MERGED: ")
# print(merge_dic)
# print(dic1)
print(d3)


