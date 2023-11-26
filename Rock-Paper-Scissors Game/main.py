rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
enemy=random.randint(0,2)

if choice == 0 :
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
print("Computer chose:\n")
enemy=random.randint(0,2)
if enemy == 0 :
  print(rock)
elif enemy == 1:
  print(paper)
elif enemy == 2:
  print(scissors)

list1 = ["d","l","w"]
list2 = ["w","d","l"]
list3 = ["l","w","d"]

wynik = [list1,list2,list3]

e = wynik[choice][enemy]
if e == "d":
  print("It's a draw")
elif e == "w":
  print("You win!")
elif e == "l":
  print("You lose")