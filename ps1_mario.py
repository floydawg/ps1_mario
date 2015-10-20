# Doing cs50 psets in python
#instead of C because I need
#practice with python for my career

# Mario Tower
height = 0
while height <= 0 or height > 23:
	height = int(raw_input("Enter a height for Mario's tower: "))

for i in range(1, height + 1):
	print " "* (height - i) + "#" * (i+1)

