import time
start_time = time.time()


print("Hello world!\nIt is a great day today!")

myInteger = 1
'''
print("How variable before math: %d\n\n" % myInteger)
myInteger = myInteger + 5
print("How variable after math: %d\n\n" % myInteger)

myFloatingPoint = 3.14
print(myFloatingPoint)

myCharacter = 'k'
print(myCharacter)

myString = "I am doing great today!"
print(myString)
'''

print(myInteger)
for counter in range(58493):
    myInteger= myInteger *2
    print(myInteger)
print(myInteger)
print("--- %s seconds ---" % (time.time() - start_time))
