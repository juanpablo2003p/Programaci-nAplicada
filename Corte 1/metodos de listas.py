animals = {'cat', 'dog', 'goldfish', 'canary', 'cat'}
print(animals) # the set will only contain one cat


even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)

# union: numbers which are big or even
print(big_numbers | even_numbers)

# intersection: numbers which are big and even
print(big_numbers & even_numbers)

print(animals)
print(sorted(animals))

# this is an empty dictionary
a = {}

# this is how we make an empty set
b = set()

# print the integers from 0 to 9
print(list(range(10)))

# print the integers from 1 to 10
print(list(range(1, 11)))

# print the odd integers from 1 to 10
print(list(range(1, 11, 2)))

animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']

animals_set = set(animals)
animals_unique_list = list(animals_set)
animals_unique_tuple = tuple(animals_unique_list)

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

colours = list(marbles) # the keys will be used by default
counts = tuple(marbles.values()) # but we can use a view to get the values
marbles_set = set(marbles.items()) # or the key-value pairs


# Python doesn't know how to convert this into a dictionary
#dict([1, 2, 3, 4])  #Uncomment to verify

# but this will work
dict([(1, 2), (3, 4)])

s = "abracadabra"

print(len(s))
print(s.index("a"))

print(s[0])
print(s[3:5])

# this will give us an error
#s[0] = "b"

print('h' in 'abcd') # False

print('ab' in 'abcd') # False

# this doesn't work for lists
print(['a', 'b'] in ['a', 'b', 'c', 'd']) # False


abc_list = list("abracadabra")
print(abc_list)

l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

s = "".join(l)
print(s)

animals = ('cat', 'dog', 'fish')

# a space-separated list
print(" ".join(animals))


# a comma-separated list
print(",".join(animals))

# a comma-separated list with spaces
print(", ".join(animals))

print("cat    dog fish\n".split())

print("cat|dog|fish".split("|"))

print("cat, dog, fish".split(", "))

print("cat, dog, fish".split(", ", 2))


my_table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(my_table[0][0])


# lists are mutable, so we can do this
my_table[0][0] = 42
print(my_table)


my_2d_list = [
    [0],
    [1, 2, 3, 4],
    [5, 6],
]
print(my_2d_list)

my_3d_list = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print(my_3d_list[0][0][0])

my_long_list = [0] * 100 # a long list of zeros
print(my_long_list)


day = [""] * 24
print(day)

timetable = day * 7
print(timetable)

timetable = [[""] * 24 for day in range(7)]
print(timetable)