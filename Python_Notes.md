# Python Notes Misc

Variable assignement and printing of different data type 
```
name = 'John'
age = 25
print(name)
print(age)
str = 'Hello Python!'
print("str1[0:5]: ", str2[1:5])
print ("Updated String: - ", str1 [:6] + 'John') 
print ("Hello this is %s and my age is %d !" % ('John', 25))
```

List(Value can be changes) and Tuples(Value can not be changed)
```
cities = ['Mumbai', 'Bangalore', 'Chennai', 'Pune']
numbers = [1, 2, 3, 4, 5, 6, 7 ]
print (cities[0])
print (numbers[1:5])
cities_tuples = ('Mumbai', 'Bangalore', 'Chennai', 'Pune')
numbers_tuple = (1,2,3,4,5,6,7)
del cities[2]
tuple1 = cities_tuple + numbers_tuple
del cities
```

Arguments in python:
The sys.argv variable is mainly used in Python scripts to access the command-line arguments provided when running the script from the terminal or command prompt.  
```
import sys
print('Number of arguments:', len(sys.argv))
print('Argument list:', str(sys.argv))
```

if, if-else, if-elif condition:
```
a = 10
if a > 0:
        print(a, "is a positive number.")
print("This statement is always printed.")


a = 10
if a > 0:
        print("Positive number")
else:
        print("Negative number")


a = 10
if a > 50:
    print("a is greater than 50")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is negative")
```

for loop for iteration
```
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for i in numbers:		# i means element in the list
        sum = sum + i
print("The sum is", sum)


for i in range(5):			# using the range function
	print("The number is", i)
```

while loop
```
a = 10
sum = 0
i = 1
while i <= a:
        sum = sum + i
        i = i + 1
print("The sum is", sum)
```






