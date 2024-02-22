import random

# 5.0 Jedi Training (50pts)  Name:Logan Mills

"""
1. Make the following program work. LIST THE 3 MISTAKES (5pts)
"""
print("This program takes three integers and returns the sum.")
total = 0
for i in range(3):
    x = int(input("Enter a number: "))  # Needs int() because it was trying to add strings
    total += x  # Was adding i each time instead of x which is the users input
print("The total is:", total)  # Printing x instead of the total

"""
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive. (5pts)
"""

for i in range(2, 101):
    print(i)

"""
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop. (5pts)
"""
countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

if countdown == 0:
    print("Blast off!")

"""
  4. Write a program that prints a random integer from 1 to 10 (inclusive). (5pts)
"""

number = random.randint(1, 10)
print(number)

'''
  5. 7 NUMBER ANALYSIS (5pts)
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''

print("Please input 7 numbers:")

number = 0
total = 0
positive = 0
negative = 0
zero = 0


for i in range(7):
    number = int(input(f"Please enter number {i+1}: "))
    total += number
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print(f"Total of numbers: {total}")
print(f"Total of Positive Numbers: {positive}")
print(f"Total of Negative Numbers: {negative}")
print(f"Total of zeros: {zero}")

'''
6. COIN TOSS PROGRAM (10pts)
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

tails = 0
heads = 0

for i in range(1, 51):
    num = random.randint(0, 1)
    if num == 0:
        print("The coin landed on tails")
        tails += 1
    else:
        print("The coin landed on heads")
        heads += 1

print("\n")
print("The coin landed on tails", tails, "times!")
print("The coin landed on heads", heads, "times!")

'''
ROSHAMBO PROGRAM (15pts)
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round, tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits, print an end game message and their win/loss/tie record

'''

done = False
wins = 0
losses = 0

while not done:
    print("1 - Rock \n2 - Paper \n3 - Scissors \n4 - Quit")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    compChoice = random.randint(1, 3)
    userChoice = int(input("Please enter a number 1-3: "))
    if userChoice > 3 or userChoice < 1:
        print("Please choose a valid number.")

    if compChoice == 1 and userChoice == 3:
        losses += 1
        print("You lost (Computer Chose Rock, You Chose Scissors)")
    elif compChoice == 1 and userChoice == 2:
        wins += 1
        print("You won (Computer Chose Rock, You Chose Paper)")
    elif compChoice == 2 and userChoice == 1:
        losses += 1
        print("You lost (Computer Chose Paper, You Chose Rock)")
    elif compChoice == 2 and userChoice == 3:
        wins += 1
        print("You won (Computer Chose Paper, You Chose Scissors)")
    elif compChoice == 3 and userChoice == 2:
        losses += 1
        print("You lost (Computer Chose Scissors, You Chose Paper)")
    elif compChoice == 3 and userChoice == 1:
        wins += 1
        print("You won (Computer Chose Scissors, You Chose Rock)")
    else:
        print("It was a tie")

    if userChoice == 4:
        done = True
