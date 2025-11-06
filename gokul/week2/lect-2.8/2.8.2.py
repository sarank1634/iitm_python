# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not

dob= int(input())
# dob = int()
current_year = 2025

age = current_year - dob

print(age)

if age >=18:
    print("your vote is elligible")
else:
    print("your not elligible for the vote")

# HINT : subtract current year from YOB