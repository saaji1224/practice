#Python program to interchange first and last elements in a list
## swap: mutually exechanging the values of the variables
def swap(l1):
    l1[0],l1[-1]=l1[-1],l1[0]
    return l1
l1=[4,6,88,9,7,5]
print(swap(l1))

##swap two elements
l=[9,5]
l[0],l[1]=l[1],l[0]
print(l)

l2=[10,2,6]
l2[0],l2[2]=l2[2],l2[0]
print(l2)

##
def sum_digits(n):
    s=0
    while n:
        s+=n%10
        n//10
    return s