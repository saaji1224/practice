l1=[[1,3,4],[5,6],[],[],4]
print([x for x in l1 if x])    ## using list comphersion (expresion context) iterate over each value in given iterable

#using filter method 
##filter() method filters the given sequence with the help of a function that tests each element in the sequence to be True or Not
##syntax  filter(function,sequence)
print(list(filter(None,l1)))
print(list(filter(lambda x:x, l1)))
print(list(filter(lambda x:x !=[],l1)))