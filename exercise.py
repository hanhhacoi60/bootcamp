from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0
 # store random number in here, each time through
i = 0  
# i should be incremented by one each iteration
while number != 5:
    i += 1
    number = randint(1,10)
    print(number)






# x = 0
# while x < 11:
# 	x += 2
# 	print(x)


# i = 1
# while i <= 5:
# 	i += 1
# 	print(i)



# times = int(input("How many times do I have to tell you?: "))

# for times in range(times):
# 	print("Clean up your room!")
# 	if times >= 10:
# 		break




# print("Type something you want to say to Sally: ")
# original = input().lower()

# while original != "stop copying me!":
# 	for i in range(1):
# 		print(original)	
# 	original = input().lower()
# print("UGH FINE CHARLIE YOU WIN")







# smiley = "\U0001f600"

# for num in range(1, 11):
# 	print(smiley * num)

# times = 1

# while times >= 1 and times < 11:
# 	print(smiley * times)
# 	times += 1








# for i in range(1,21):
# 	if i == 4 or i == 13:
# 		print(f"{i} is unlucky :(")
# 	elif i % 2 == 1:
# 		print(f"{i} is an odd number")
# 	else:
# 		print(f"{i} is an even number")

# for i in range(1,21):
# 	if i == 4 or i == 13:
# 		state = "unlucky"
# 	elif i % 2 == 1:
# 		state = "odd"
# 	else:
# 		state = "even"
# 	print(f"{i} is {state}")