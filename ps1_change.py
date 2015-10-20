#prints out how many coins a customer can expect with
#a user-entered amount of change requsted

change = 0
coins = 0
while change <= 0:
	change = float(raw_input("Enter the amount of change expected: "))

round(change, 2)

change_in_cents = change * 100.0

while change_in_cents > 0:
	# get number of quarters
	quarters = change_in_cents // 25
	coins += quarters
	change_in_cents = change_in_cents - (quarters * 25)
	# get number of dimes
	dimes = change_in_cents // 10
	coins += dimes
	change_in_cents = change_in_cents - (dimes * 10)
	# get number of nickels
	nickels = change_in_cents // 5
	coins += nickels
	change_in_cents = change_in_cents - (nickels * 5)
	# pennies are all that are left
	coins += change_in_cents
	change_in_cents = 0

print int(coins)

