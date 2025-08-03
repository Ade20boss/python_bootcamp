first = input("Name of guy: ").upper()
second = input("Name of lady: ").upper()
t_count = 0
r_count = 0
u_count = 0
e_count = 0
l_count = 0
o_count = 0
v_count = 0
combined_names = first + second

for i in combined_names:
	if i == "T":
		t_count += 1
	if i == "R":
		r_count += 1
	if i == "U":
		u_count += 1
	if i == "E":
		e_count += 1
	
for letter in combined_names:
	if letter == "L":
		l_count += 1
	if letter == "O":
		o_count += 1
	if letter == "V":
		v_count += 1
		

print(f"T occurs {t_count} times")
print(f"R occurs {r_count} times")
print(f"U occurs {u_count} times")
print(f"E occurs {e_count} times")

total1 = t_count + r_count + u_count + e_count
print(f"Total = {total1}")

print(f"L occurs {l_count} times")
print(f"O occurs {o_count} times")
print(f"V occurs {v_count} times")
print(f"E occurs {e_count} times")

total2 = l_count + o_count + v_count + e_count
print(f"Total = {total2}")

love_score = str(total1) + str(total2)
print(f"Love Score = {love_score}")

love_score = int(love_score)

if love_score < 10 or love_score > 85:
	print("Your score is x, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 70:
	print("Your score is y, you are alright together.")
else:
	print("Your score is " + str(love_score))


