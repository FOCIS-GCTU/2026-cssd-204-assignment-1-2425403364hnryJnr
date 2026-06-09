# File: bowling.py
# Description: Calculates a bowler's average and handicap after three games
# Assignment Number: 4
#
# Name:  Henry Brandford-Arthur Junior
# SID:   2425403364
# Email: 2425403364@live.gctu.edu.gh
# Grader: Mr.Augustus Buckman
# Slip days used this assignment: 0
#
# On my honor, Henry Brandford-Arthur Junior, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    name = input("Enter your name: ")

    game1 = int(input("Enter Game 1: "))
    game2 = int(input("Enter Game 2: "))
    game3 = int(input("Enter Game 3: "))

    average = (game1 + game2 + game3) // 3
    handicap = (200 - average) * 80 // 100

    print(name + "'s average is: " + str(average))
    print(name + "'s handicap is: " + str(handicap))

main()
