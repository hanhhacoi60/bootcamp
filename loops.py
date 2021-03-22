sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
# My answer, which was less efficient, uses a while loop
i = 0
result = ''
while i < len(sounds):
    result += sounds[i]
    i += 1
result = result.upper()
print(result)

#Here is the corrent answer, which uses a for loop
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()