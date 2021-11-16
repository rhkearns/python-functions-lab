#1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n

def sum_to(n):
  count = 1
  sum = 0
  while count <= n:
    sum += count
    count += 1
  return sum

print(sum_to(6))
print(sum_to(10))

#2. Write a function named largest that takes a list of numbers as an argument and returns the largest nubmer in that list

def largest(items):
  biggest = items[0]
  for item in items:
    if biggest < item:
      biggest = item
  return biggest

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))


#3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string

def occurances(str1, str2):
  return str1.count(str2)


print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

#4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together and reutns the product. HINT: review notes on args

def product(*args):
  result = 1
  for arg in args:
    result *= arg
  return result

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))
