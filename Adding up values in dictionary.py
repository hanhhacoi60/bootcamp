# Modern Python 3 Bootcamp
#Coding Exercise 28
# Goal is to add up the total donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)

# My method (ends up being super inefficient)
total = []
for amount in donations.values():
    total.append(amount)
total_donations = sum(total)
print(total_donations)

# Solution 1:
total_donations1 = 0
for donation in donations.values():
    total_donations1 += donation
print(f"The total is ${total_donations1}")

# Solution 2: uses built-in function called sum()
total_donations2 = sum(donation for donation in donations.values())
print(total_donations2)

# Solution 3: most efficient!!
total_donations3 = sum(donations.values())
print(total_duonations3)
