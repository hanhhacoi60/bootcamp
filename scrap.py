instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number"
}

y = instructor.get('name')
print(y)


d = dict(a=1, b=2, c=3)

the = d['a']
print(the)

the1 = d.get('a')
print(the1)

floor = d['b']
print(floor)
floor1 = d.get('b')
print(floor1)

lava = d['no_key']
print(lava)

lava1 = d.get('no key')
print(lava1)


# x = {}.fromkeys("a", "b")

# y = {}.fromkeys(["email"], 'unknown')

# z = {}.fromkeys("a", [1, 2, 3, 4, 5])

# print(x, y, z)

# z = {}.fromkeys(range(1, 6), 'unknown')
# print(z)
