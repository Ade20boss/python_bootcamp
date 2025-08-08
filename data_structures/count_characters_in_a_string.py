def count_letter(word, letter):
	freq_of_letters = 0
	word = word.lower()
	for i in word:
		if i == letter:
			freq_of_letters += 1
	return freq_of_letters

print(count_letter("table", "b"))

