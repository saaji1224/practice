#Python program to find the sum of all items in a dictionary
# sum() method will return the sum of all values in the dictionary.
d1={"a":80,"b":42,"c":3,"d":56}
print("Dictionary:",d1)
print("sum:",sum(d1.values()))

def sum(d2):
    sum=0
    for j in d2.values():
        sum=sum+j
    return sum
d2={"a1":34,"b1":10,"c1":30}
print('dictionary:',d2)
print("sum:",sum(d2))