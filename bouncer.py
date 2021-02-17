# code-along in the The Modern Python 3 Bootcamp with Colt Steele

#ask for age
age = input("How old are you: ")

## add an if statement to prevent errors if someone doesn't input anything
# this is one way to make an if statement  --> if age != "":
# a quicker way to make an if statement is to take advantage of the fact that empty strings are falsy
if age:
	age = int(age)
	#18-21 wristband
	if age >= 18 and age < 21:
		print("You can enter, but need a wristband!")
	#21+ drink, normal entry
	elif age >= 21:
		print("You can enter and can drink!")
	# too young, sorry
	else:
		print("Sorry, you're too young for this rodeo wee one.")
else:
	print("Please enter an age.")


#Here is a more succinct way to write the code:
# age = input("How old are you: ")
# if age:
# 	age = int(age)
# 	if age >= 21:
# 		print("You can enter and can drink!")
# 	elif age >= 18:
# 		print("You can enter, but need a wristband!")
# 	else:
# 		print("Sorry, you're too young for this rodeo wee one.")
# else:
# 	print("Please enter an age.")