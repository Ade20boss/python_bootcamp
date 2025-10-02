def convert_grade(dictionary):
	for key in dictionary:
		if 85 <=  dictionary[key] <= 100:
			dictionary[key] = "Outstanding"
		elif 65 <= dictionary[key] <= 84:
			dictionary[key] = "Good"
		elif 50 <= dictionary[key] <= 64:
			dictionary[key] = "Acceptable"
		else:
			dictionary[key] = "Fail"
	print(dictionary)

student_scores = {
  "John": 90,
  "Edy": 68,
  "Marry": 88, 
  "Ewan": 79,
  "Park": 62,
}
convert_grade(student_scores)
