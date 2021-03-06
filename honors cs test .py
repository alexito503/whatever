# Honors Computer Science Test

import os
from time import sleep
from sys import platform, exit

def start_page(): 
  print("Welcome to MyBelen")
  user_input = input("What would you like to do?\n\nAdd a student (1)\nLook for a student (2)\nDelete a student (3)\nExit the tool (4)\n\nOption: ")
  if user_input == "1":
    addStudent()
  elif user_input == "2":
    LStudent()
  elif user_input == "3":
    delStudent()
  elif user_input == "4":
    print("Now exiting the tool in 2 seconds!")
    sleep(2)
    exit()

def addStudent():
  sName = input("Enter student name: ")
  sGender = input("Enter student gender: ")
  sHeight = int(input("Enter student height(in inches): "))
  sWeight = int(input("Enter student weight: "))
  sgpa = (input("what was your gpa last year: "))

  grade1 = int(input("Enter Grade 1: "))
  grade2 = int(input("Enter Grade 2: "))
  grade3 = int(input("Enter Grade 3: "))
  grade4 = int(input("Enter Grade 4: "))
  grade5 = int(input("Enter Grade 5: "))
  grade6 = int(input("Enter Grade 6: "))
  grade7 = int(input("Enter Grade 7: "))
  f = open(f"{sName}.txt", "w+")
  f.write(f"Name: {sName}\nGender: {sGender}\nHeight: {sHeight}\nWeight: {sWeight}\nGPA: {sgpa}\nGrade 1: {grade1}\nGrade 2: {grade2}\nGrade 3: {grade3}\nGrade 4: {grade4}\nGrade 5: {grade5}\nGrade 6: {grade6}\nGrade 7: {grade7}")
  f.close()
  print("Added student!\n\nGoing back to main menu in 2 seconds!")
  sleep(2)
  start_page()

def delStudent():
    del_input = input("Which student would you like to terminate?: ")
    if os.path.exists(f"{del_input}.txt"):
        os.remove(f"{del_input}.txt")
        start_page()
    else:
        print(f"{del_input}.txt does not exist!")
        sleep(2)
        print("Going back to the start page in 5 seconds...")
        sleep(5)
        if platform == "linux" or platform == "linux2":
            # Linux
            os.system('clear')
        elif platform == "darwin":
            # MacOS
            os.system('clear')
        elif platform == "win32":
            # Windows
            os.system('cls')
        start_page()

def LStudent():
    look_input = input("What's the name of the student you're looking for?: ")
    if os.path.exists(f"{look_input}.txt"):
        with open(f"{look_input}.txt", "r") as f:
            print("Here's your info!\n\n")
            print(f.read())
            print()
            f.close()
            print("Going back to the main menu now in 2 seconds now!")
            sleep(2)
            start_page()
    else:
        print(f"{look_input}.txt doesn't exist!")
        sleep(2)
        print("Going back to the start page in 5 seconds...")
        sleep(5)
        if platform == "linux" or platform == "linux2":
            # Linux
            os.system('clear')
        elif platform == "darwin":
            # MacOS
            os.system('clear')
        elif platform == "win32":
            # Windows
            os.system('cls')
        start_page()

start_page()









