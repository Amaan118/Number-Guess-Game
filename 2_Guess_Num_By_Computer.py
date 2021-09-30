import random

low = 1
high = 100
att = 0

while True:
	att += 1
	num = random.randint(low, high)
	print("Number : " + str(num))
	ask = int(input("1.Go High \t2.Go Low \t3. Correct \n"))

	if ask == 1:
		low = num+1
	elif ask == 2:
		high = num-1
	else:
		print(f"Number to Guess : {num} \nAttempts : {att}")
		exit()