# Write a program to accept the positive integer n from the user and print counting of numbers which are not

# prime from 1 to n.

n = int(input("enter a positive integer: "))

non_prime_count = 0

for num in range(1, n+1):
    if num <= 1:
        # 1 and numbers <=1 are not prime
        non_prime_count += 1
        continue
    
    # check if number is prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if not is_prime:
        non_prime_count += 1

print(f"Number of non-prime numbers from 1 to {n} is {non_prime_count}")