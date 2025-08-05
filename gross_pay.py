def compute_pay(p_hour, p_rate):
	if p_hour <= 40:
		pay = round(hours * rate, 2)
		
	else:
		overtime = p_hour - 40
		overtime_pay = (p_rate * 1.5) * overtime
		pay = round((p_hour - overtime) * p_rate, 2) + overtime_pay
	return pay

def check_for_float(p_input):
	try:
		val = float(p_input)
	except ValueError:
		print("Error, Enter numeic input")
		quit()
		

hours = (input("Enter Hours: "))
check_for_float(hours)
rate = (input("Enter Rate: "))
check_for_float(rate)
hours = float(hours)
rate = float(rate)


output = compute_pay(hours, rate)

print(f"Pay: {output}")
