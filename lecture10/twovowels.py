# Read a string from STDIN until * is entered
# Count and show the stretch of 2-vowels in the string (Matching words)
# A stretch of 2-vowels is: a segment of a word after a 'z' or a word; containing exactly 2 vowels
# Example: 
# String: azoooza azooza zoo azoo
# Matching words: 3
# String: GONZALEZ passes the ball to VAZQUEZ
# Matching words: 3 
# String: azozozee
# Matching words: 1  (here the segment zee is the match)
# Recommended approach, use the break-it-down build-it-up process

# step 1: count the vowels in a segment (string) 
# This function returns the total number of vowels in a string
def vowel_count(segment):
	count = 0
	for c in segment:
		if c in 'aeiou':
			count += 1
	return count 

# step 2: check if there is 2 vowels after a 'z'
# This function splits a string using 'z' as delimeter
def match_word(word):
	for segment in word.split('z'):
		if vowel_count(segment) == 2:
			return True 
	return False

# step 3: check if sentence has matching words (contain 2 vowels)
# This function split the sentence into words and count the matching words
def word_count(sentence):
	count = 0
	for word in sentence.split(' '):
		if match_word(word):
			count +=1
	return count

# main function: read until * and show the number of matches
def show_matches():
	sentence = input('sentence: ')

	while sentence != '*':
		print(f'mMatching words: {word_count(sentence.lower())}')
		sentence = input('sentence: ')

show_matches()

