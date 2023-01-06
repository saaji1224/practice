#Find the size of a Dictionary in Python
#find the size of dictionary is two ways 
#one is getsizeof() and __sizeof__()
import sys
dic2 = {"aws": "vpc", "linux": "ls", "python": "boto3"}
dic3 = {1: "sajith", 2: "saida", 3: "gouse", 4: "mohiddion"}

# print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
# print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")

print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")