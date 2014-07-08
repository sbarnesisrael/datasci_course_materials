import re

#MAP
def mapper(function, sequence):
	# list to store the results of the map operation
	result = []
	
	# iterate over each item in sequence, append the values to the results list
	# after they have been modified by the "function" supplied as an argument in the
	# mapper function call.
	for item in sequence:
		result.append(function(item))
		
	return result
	
def reducer(function, sequence, base_value):
	# Need to get a base value to serve as the starting point for the construction
	# of the result.
	# Assuming one is given, but in most cases you should include extra validation
	# here to either ensure one is given, or some sensible default is chosen
	accum_value = base_value
	
	# iterate thru the sequence items, applying the "function" provided, and
	# storing the results in the accum_value object
	for item in sequence:
		accum_value = function(item, accum_value)
		
	return accum_value
	
# With these functions it should be sufficient to address the problem, what remains
# is simply to get the data from the text files, and keep track of the lines in which
# words appear.
if __name__ == 'main':
	word_list_file = 'AFINN-111.txt'
	
	# Read in a file containing the words that will be searched in the text file
	# (assumes words are given as a CSV)
	infile = open(word_list_file, 'rt')
	content = infile.read()
	word_list = content.split(',')
	infile.close()
	
	target_text_file = 'tweets.txt'
	
	# Read in the text to analyze
	infile = open(target_text_file, 'rt')
	target_text_lines = infile.readlines()
	infile.close()
	
	# With data loaded, the overall strategy will be to loop over the text lines
	# and we will use the map function to loop over the word_list and see if they
	# are in the current text file line
	
	# First, define the my_mapper function that will process your data, and will be 
	# passed to the map function
	def my_mapper(item):
		# Split the current sentence into words
		# Will split on any non alpha-numeric character. This strategy can be revised
		# to find matches to a regular expression pattern based on the words in the 
		# words list. Either way, make sure you choose a sensible strategy to do this.
		current_line_words = re.split(r'\W+', target_text_lines[k])
		
		# lowercase the words
		current_line_words = [words.lower() for word in current_line_words]
		
		# check if the current item (word) is in the current_line_words list, and if so,
		# return the word and the line number
		if item in current_line_words:
			return [item, k+1] # return k+1 because line numbers start at 0, but humans start at 1.
		else:
			return []
			
	# With mapper function established, we can proceed to loop over the text lines
	# of the array, and use our map function to process the lines against the list of words.
	
	# This array will store the results of the map operation
	map_output = []
	
	# Loop over text file lines, use mapper to find which words are in which lines, store 
	# in map_output list. This is the exciting stuff!
	for k in range(len(target_text_lines)):
			map_output.extend(mapper(my_mapper, word_list))

	# At this point, we should have a list of lists containing the words and the lines they 
	# appeared in, and it should look like, [['word1', 1] ... ['word25': 5] ... [] ...]
	# As you can see, the post-map array will have an entry for each word that appeared in 
	# each line, and if a particular word did not appear in a particular line, there will be a
	# empty list instead.

	# Now all that remains is to summarize our data, and that is what the reduce function is 
	# for. We will iterate over the map_output list, and collect the words and which lines 
	# they appear at in an object that will have the format { 'word': [n1, n2, ...] },where 
	# n1, n2, ... are the lines the word appears in. As in the case for the mapper
	# function, the output of the reduce function can be modified in the my_reducer function 
	# you supply to it. If you'd rather it return something else (like say, word count), this
	# is the function to modify.

	def my_reducer(item, accum_value):
			# First, verify item is not empty
			if item != []:
					# If the element already exists in the output object, append the current line 
					# value to it, if not, add it to the object and create a set holding the current 
					# line value

					# Check this word/line combination isn't already stored in the output dict
					if (item[0] in accum_value) and (item[1] not in accum_value[item[0]]):
							accum_value[item[0]].append(item[1])
					else:
							accum_value[item[0]] = [item[1]]

			return accum_value

	# Now we can call the reduce function, save it's output, print it to screen, and we're  
	# done!
	# (Note that for base value we are just passing in an empty object, {})
	reduce_results = reducer(my_reducer, map_output, {})

	# Print results to screen
	for result in reduce_results:
			print('word: {}, lines: {}'.format(result, reduce_results[result]))