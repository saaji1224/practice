count=0
for i in range(1,100):
    if ((i%2==0) & (i%3==0)):
        print(i)
        count=count+1
print(count)


# n=1234
# print(len(str(n)))

n=int(input("enter the number:"))
count=0
while n>0:
    count+1
    n=n//10
print(count)