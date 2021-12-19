with open('data') as f:
	data = [int(x) for x in f]

print(sum(x < y for x, y in zip(data, data[1:])))
print(sum(x < y for x, y in zip(data, data[3:])))
