## Basic syntax with Python ##

####################################################
# For
arr = ['A', 'B', 'C']
for i in arr:
  print(str(i))

####################################################
# Range
# To 10
for i in range(10):
	print(i)

# 10 to 20 every 2
for i in range(10, 20, 2):
	print(i)

####################################################
# Input
# num1 = input('Digite um numero: ')
# print(num1)

####################################################
# Append
arr = []
arr.append('textToAddInArray')
print(arr)

####################################################
# Verify list
arr = [1, 2, 3]
if 2 in arr:
	print('2 in list')

####################################################
# Remove elements
# Remove index 3 to index 4: 3, 4 and 5
arr = [1, 2, 3, 4, 5, 6]
del arr[2:4]
print(arr)

# Remove index 3 to end: 4, 5 and 6
arr = [1, 2, 3, 4, 5, 6]
del arr[2:]
print(arr)

####################################################
# Sort list
arr = [4, 2, 1, 3]

# return sorted new list
arr2 = sorted(arr)
print(arr)
print(arr2)

# ascending
arr.sort()
print(arr)

# descending
arr.sort(reverse=True)
print(arr)

####################################################
# Dictionary
d = { 'keyA': 1, 'keyB': 2 }
print(d['keyA'])

# return tuple
for i in d.items():
  print(i)

# return values 1 and 2
for i in d.values():
  print(i)

# return values keyA and keyB
for i in d.keys():
  print(i)

####################################################
# Funtion
def toPrint(param):
  print(param)
toPrint('Hello World')

####################################################
# File
file = open('file.txt')
lines = file.readlines()
print(lines)

# read
file = open('file.txt')
content = file.read()
print(content)
file.close()

# write
newFile = open('file2.txt', 'w')
newFile.write('Text on file 2')
newFile = open('file2.txt')
print(newFile.read())
newFile.close()

# append
newFile = open('file2.txt', 'a')
newFile.write('\nNew text on file 2')
newFile = open('file2.txt')
print(newFile.read())
newFile.close()

####################################################
# Exception
a = 2
b = 0
try:
  print(a/b)
except:
  print('Message error')

####################################################
# Random
import random

num = random.randint(0, 10)
print(num)

# choice
arr = [5, 10, 15, 20]
num = random.choice(arr)
print(num)
