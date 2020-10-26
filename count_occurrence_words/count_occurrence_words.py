# Parse the dictionary file dictionary.txt
# Check the alice.txt file as input and count the number of occurences of any word in the dictionary file that appears in the input stream.
# Author : Dung Ho

import re
import collections


# Define a function that pares 'Dictionary.txt' file
def dictionary(f_name):
	# Open a text file which is used as a dictionary
	dictionary = (open(f_name,'r')).readlines()
	
	# Create a new list that stores every line in dictionary, ignores empty line and a line starting with '#'
	filtered_dcitionary = []
	for line in dictionary:
		if line[0] != '#':
			if line == '\n':
				pass
			else:
				filtered_dcitionary.append(line.strip())
				
	return filtered_dcitionary

	
# Define a function that parse a 'alice.txt' file
def book(f_name):
	# Open text file with all special characters
	unclean_book = open(f_name).read().lower()
	
	# Remove all special characters 
	clean_book = (re.sub('[^A-Za-z0-9\s]+', '', unclean_book)).split()
	
	# Count how many words appear in the book and the number of appear
	count_book = collections.Counter(clean_book)

	# Return a dictionary with the key are the words appear and values are the number of appear
	return count_book
	


# Define a function that check occurences words from book (alice.txt) and dictionary (dictionary.txt)
def check_occurrences(book, dictionary):
	# Sort book and dictionary by alphabet
	sorted_book = sorted(book)
	sorted_dictionary = sorted(dictionary)
	
	# Create a new empty dictionary to store the occurrenced words and the number of occurrences
	occurrenced_dict = {}
	
	i = 0			# index of word in book
	j = 0			# index of word in dictionary
	
	# Perform binary search to check words in book that occur in dictionary
	while i < len(sorted_book) and j < len(sorted_dictionary):
		if sorted_book[i] == sorted_dictionary[j]:
			occurrenced_dict[sorted_book[i]] = book[sorted_book[i]]
			i += 1
			j += 1
		elif sorted_book[i] > sorted_dictionary[j]:
			j += 1
		else:
			i += 1
			
	return occurrenced_dict

# Print out 'Dictionary.txt' as a line a single word
print('Dictionary: ')
print('-' * 40)
# Using arbitrary function *agrs and separate by line
# print(*agrs, sep ='\n')
print(*dictionary('dictionary.txt'), sep = '\n')

# Print out the occurrences words list
occur_dict = check_occurrences(book('alice.txt'), dictionary('dictionary.txt'))
sorted_occur_dict = sorted(occur_dict.items(), key = lambda x: x[1])

print('\n\n')
print('-' * 40)
print('{: <30s} {: <5s} '.format('Number of occurrences', 'Words'))
print('-' * 40)
for x in sorted_occur_dict:
	print('{: <30d} {: <5s} '.format(x[1], x[0]))

print('\n')
print('Total of occurrences words')
print('-' * 40)
print('{: <30d} {: <5s} '.format(sum(occur_dict.values()), 'Total Words'))
