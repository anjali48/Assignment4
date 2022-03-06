Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.



sample input: 10

sample output: 35
add=lambda x,y=25:x+y
print(add(10))
35
Write a Python program to triple all numbers of a given list of integers. Use Python map.



sample list: [1, 2, 3, 4, 5, 6, 7]



Triple of list numbers:

[3, 6, 9, 12, 15, 18, 21]
lis= [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda v:(v*3),lis)))
[3, 6, 9, 12, 15, 18, 21]
Write a Python program to square the elements of a list using map() function.



Sample List: [4, 5, 2, 9]

Square the elements of the list:

[16, 25, 4, 81]
l= [4, 5, 2, 9]
print(list(map(lambda i:(i**2),l)))
[16, 25, 4, 81]