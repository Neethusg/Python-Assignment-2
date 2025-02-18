Assignment 2

# Topic :List
#Exercise 1
# Q1. Create a list of 5 random numbers and print the list.

import random
random_numbers = [random.randint(1, 50) for i in range(5)]

print("List of 5 random numbers:", random_numbers)

# Q2. Insert 3 new values to the list and print the updated list.

random_numbers.insert(0, 51)
random_numbers.insert(1,52)
random_numbers.insert(2, 65)

print("Updated list after inserting 3 values:", random_numbers)

# Q3. Try to use a for loop to print each element in the list

print("Printing each element in the list:")
for number in random_numbers:
    print(number)

#Topic: Dictionary
#Exercise
#Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

details = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}
print(details)

#Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

details['phone'] = '1234567890'

print(details)

#Topic: Set
#Exercise
#Q1.Create a set with values 1, 2, 3, 4, and 5.

set = {1, 2, 3, 4, 5}

print(set)

# Q2. Add the value 6 to the set created in Q1.

set.add(6)
print(set)

# Q3. Remove the value 3 from the set created in Q1.

set.remove(5)
print(set)

# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4

tuple = (1, 2, 3, 4)

print(tuple)

# Q2. Print the length of the tuple created in Q1

tuple_length = len(tuple)
print("Length of the tuple:", tuple_length)

