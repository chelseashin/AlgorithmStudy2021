n = int(input())
data = [['*']*n for _ in range(n)]

def remove_stars(length, x, y):
	global data
	if length == 1:
		return
	for row in data[x-length+length//3: x-length//3]:
		row[y-length+length//3:y-length//3] = ' '*(length//3)
	for i in range(length//(length//3)):
		for j in range(length//(length//3)):
			remove_stars(length//3, x-i*length//3, y-j*length//3)

remove_stars(n, n, n)
for row in data:
	print(''.join(row))