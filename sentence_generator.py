import random
import sys

def generate_sentences(number_of_sentences, input_file, output_file):
	titles, title_values = read_input(input_file)
	sentences = build_sentence(number_of_sentences, titles, title_values)
	write_output(sentences, output_file)


def read_input(input_file):
    '''
    Read the contents of the input file into data structures to be used for random sampling later
    '''
	print 'generating sentences from words in ', input_file, '...'

	input_file = open(input_file, 'r')
	Lines = input_file.readlines()
	input_file.close()

	title_values = {}
	titles = []

	for line in Lines:
		split = line.split('=')
		title = split[0].strip() # TODO: add support for cases where the word list has no title/key/label
		titles.append(title)
		values = map(lambda x: x.strip(), split[1].split(","))
		title_values[title] = values

	return titles, title_values


def write_output(sentences, output_file):
    '''
    Write the sentences to the provided output file
    '''
	print 'writing sentences to ', output_file
	output_file = open(output_file, 'w')
	output_file.writelines(map(lambda sentence: sentence + '\n', sentences)) # append new line character before writing each line
	output_file.close()


def build_sentence(number_of_sentences, titles, title_values):
    '''
    Build sentences as permutations from each title
    '''
	print 'number of sentences to be generated is', number_of_sentences

	sentences = []
	for i in range(number_of_sentences):
		sentence = ''
		for title in titles:
			possible_words = title_values.get(title)
			random_word = random.choice(possible_words)
			if random_word: # if string is not empty, pad with space
				random_word += ' '
			sentence += random_word

		sentences.append(sentence.strip())

	return sentences

if __name__ == "__main__":
	number_of_sentences = int(sys.argv[1])
	input_file = sys.argv[2].strip()
	output_file = sys.argv[3].strip()
	generate_sentences(number_of_sentences = number_of_sentences, input_file = input_file, output_file = output_file)
