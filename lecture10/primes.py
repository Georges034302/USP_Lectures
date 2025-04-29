# def <function-name> (args - if needed):
# 	code 
# 	return (if a value should be returned)

# Requirements:
# 1 - Generate a randon list ef integers
#       - size n from STDIN
#       - start value from STDIN
#       - end value from STDIN
# 2 - Check if a number is prime
# 3 - Determine the prime list from the random list
# 4 - Show both lists

import random as ran 

# step 1: returns a random list
def random_list(size,start,end):
	return ran.sample(range(start,end+1),size)


# step 2: check if an integer is prime
def is_prime(n):
	for e in range(2,n):
		if n%e == 0:
			return False
	return True

# step 3: determine prime-list from any list (of numbers)
def prime_list(numbers):
	primes = []
	for e in numbers:
		if is_prime(e):
			primes.append(e)
	return primes

# step 4: create and show numbers and primes
def run():
	start = int(input('start: '))
	end = int(input('end: '))
	size = int(input('size: '))
	numbers = random_list(size,start,end)
	print(numbers)
	print(prime_list(numbers))

run() # main function that runs all the script
