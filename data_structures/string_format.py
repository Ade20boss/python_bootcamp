names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]
print(f'{"Name":<10} {"Score":<5}')
for index in range(len(names)):
	print(f"{names[index]:<10} {scores[index]:<5}")