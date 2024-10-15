#!/bin/env python3

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

def vowel_count(segment):
    count = 0
    for c in segment:
        if c in 'aeiou': # means c is a vowel
            count += 1
    return count         # returning the total vowel count in a string

def matching_word(word):
    for segment in word.split('z'):     # break down words into segments if z is found in a word
        if vowel_count(segment) == 2:   # check if a segment contains 2 vowels
            return True
    return False
    
def word_count(sentence):
    count = 0
    for word in sentence.split(' '):    # break down a sentence into multiple words
        if matching_word(word):         # finding the words containing 2 vowels
            count += 1
    return count                        # This is the actual count of matching words

def show_matches():
    sentence = input('Sentence: ')
    while sentence != '*':
        print(f'Matching words: {word_count(sentence.lower())}')
        sentence = input('Sentence: ')

show_matches()








