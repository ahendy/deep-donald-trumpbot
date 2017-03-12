import markovify
d1 = 'deeptrump.txt'
d2 = 'manualtrump.txt'
d3 = 'deeptrump3.txt'
with open(d2) as f:

	text = f.read()
	# Build the model.
	text_model = markovify.Text(text)

	# Print five randomly-generated sentences
	# for i in range(5):
	    # print(text_model.make_sentence())

	# Print three randomly-generated sentences of no more than 140 characters
	for i in range(3):
	    print(text_model.make_short_sentence(140))