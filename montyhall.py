from random import randint
def montyhall(firstdoor="duck", switchornot="duck"):
	"""
	This function can be called with no parameters, so you can play the game, or with params to simulate the games
	"""
	sim = False
	if firstdoor == "duck" or switchornot == "duck":
		sim = True
	doors = ["", "", ""]
	cardoor = randint(0,2)
	doors[cardoor] = "car"
	for idx, door in enumerate(doors):
		if door != "car":
			doors[idx] = "goat"
	if sim:
		print("You're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.")
		print("D D D")
		print("1 2 3")
	firstpick = 999
	if sim:
		firstpick = int(input("Pick a door: ")) - 1
	else:
		firstpick = int(firstdoor) - 1
	if sim:
		print("I will now open a door!")
	others = doors
	st = others[firstpick]
	others[firstpick] = "none"
	notfound = True
	reveal = 0
	while notfound:
		r = randint(0,2)
		if others[r] == "goat":
			reveal = r
			notfound = False
	if sim:
		print("Door "+str(reveal+1)+" is a goat!")
	newprint = doors
	pstr = ""
	for idx, np in enumerate(newprint):
		if idx != reveal:
			if pstr == "":
				pstr = "D"
			else:
				pstr = pstr + " D"
		else:
			if pstr == "":
				pstr = "G"
			else:
				pstr = pstr + " G"
	if sim:
		print(pstr)
	if sim:
		switch = input("You selected door "+str(firstpick+1)+" would you like to change? (y/n): ")
	else:
		switch = switchornot
	newpick = "no"
	if switch == "y":
		ndoors = doors
		pdoo = ""
		for idx, nd in enumerate(ndoors):
			if idx != reveal and idx != firstpick:
				pdoo = str(idx + 1)
				newpick = doors[idx]
		if sim:
			print("You have switched to door "+pdoo)
			print(newpick)
		else:
			return newpick
	else:
		if sim:
			print("You have stayed with door " + str(firstpick+1))
			print(st)
		else:
			return st
"""
This code calls the sim function tons of times and displays the results
"""
#Settings
switchfail = 0
switchwin = 0
switchtimes = 10000
stayfail = 0
staywin = 0
staytimes = 10000
#Don't touch code below unless you know what you are doing.
for i in range(switchtimes):
	mh = montyhall(randint(1,3), "y")
	if mh == "car":
		switchwin = switchwin + 1
	else:
		switchfail = switchfail + 1
for i in range(staytimes):
	mh2 = montyhall(randint(1,3), "n")
	if mh2 == "car":
		staywin = staywin + 1
	else:
		stayfail = stayfail + 1
print("== MONTY HALL ==")
print("Switching "+str(switchtimes)+" times")
print("Staying "+str(staytimes)+" times")
print("=== RESULTS ===")
print("Switch: "+str((switchwin/switchtimes) * 100)+"% win, "+str(switchfail/switchtimes)+"% lose")
print("Stay: "+str((staywin/staytimes) * 100)+"% win, "+str(stayfail/staytimes)+"% lose")
