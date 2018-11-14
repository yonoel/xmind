x=[a for a in range(10) if a%2 == 1]
print(x)
listofCountries = ["India","America","England","Germany","Brazil","Vietnam"]
firstLetters = [ country[0] for country in listofCountries ]
print(firstLetters)
print ([x+y for x in 'get' for y in 'set'])
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
oddMonths = [iter for index, iter in enumerate(months) if (index%2 == 0)]
print(oddMonths)
two_dim_list = [ [0]*3 ] *3
print(two_dim_list)
theList = [1, 2, 3, 4, 5, 6, 7, 8]
print(theList[::2])
print(theList[::-1])
print(theList[::-2])
for element in theList:
 print(element)
vowels = ['a','e','i','o','u']

vowels.remove('a')

# Result: ['e', 'i', 'o', 'u']
print(vowels)

# Result: 'i'
print(vowels.pop(1))

# Result: ['e', 'o', 'u']
print(vowels)

# Result: 'u'
print(vowels.pop())

vowels = ['a','e','i','o','u']

vowels[2:3] = []
print(vowels)

vowels[2:5] = []
print(vowels)
theList = ['a','e','i','o','u']
theList.sort(reverse=True)
print(theList)

theList = ['a','e','i','o','u']
print('------------------')
print(theList[0:len(theList)])
print(theList[0:5])
print('------------------')
newList = sorted(theList, reverse=True)
print("Original list:", theList, "Memory addr:", id(theList))
print("Copy of the list:", newList, "Memory addr:", id(newList))


