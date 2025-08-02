hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = 0
if hours <= 40:
	pay = round(hours * rate, 2)
	print(f"Your pay is {pay}")
elif hours > 40:
	overtime = hours - 40
	overtime_pay = (rate * 1.5) * overtime
	pay = round((hours - overtime) * rate, 2) + overtime_pay
	print(f"You worked for more than 40 hours, your payment plus overtime is: {pay}")
	




