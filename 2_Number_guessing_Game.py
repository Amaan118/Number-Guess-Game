import random
import time

num = random.randint(1, 100)
user = -1
attempt = 0

while (user != num):
    user = int(input("Enter a Number : "))
    if num > user:
        print("Please Enter a Greater Number")
    elif num < user:
        print("Please Enter a Smaller Number")
    attempt += 1

with open("2_Record_number_guess.txt","a") as f:
    f.write("\n")
    f.write(f"Date : {time.asctime(time.localtime(time.time()))}")
    f.write(f"\nNumber to Guess : {num} \nAttempts Taken : {attempt}")
    f.write("\n")
