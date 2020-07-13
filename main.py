print("Enter Input String:")
inputStr = input()


for i in range(len(inputStr)):
	count = 0
	for j in range(len(inputStr)):
		if inputStr[i].lower() == inputStr[j].lower():
			count = count + 1;
	if count == 1:
		result = str(inputStr[i])
		inputStr = inputStr.replace(inputStr[i], '')
		break


d = {}

for i in range(len(inputStr)):
	Upper = 0
	if inputStr[i].isupper():
		Upper = 1;
	if inputStr[i].lower() not in d:
		if Upper == 1:
			d[inputStr[i].lower()] = inputStr[i].upper()
		else:
			d[inputStr[i].lower()] = inputStr[i].lower()
	else:
		if Upper == 1:
			d[inputStr[i].lower()] = d[inputStr[i].lower()] + inputStr[i].upper()
		else:
			d[inputStr[i].lower()] = d[inputStr[i].lower()] + inputStr[i].lower()

for k in sorted(d, key=lambda k: len(d[k])):
	result = result + d[k]


print(result)
