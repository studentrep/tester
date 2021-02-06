#Towers of Hanoi project
#Lesson: Stacks
from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

#Add stacks to the list of stacks
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game

num_disks = int(input("\nHow many disks do you want to play with?\n"))

#Ensure that the user is playing a game with at least 3 disks
while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3. \n"))

#push the number of disks requested onto the leftmost stack
for i in range(num_disks,0,-1):
  left_stack.push(i)

#left_stack.print_items()

#Calculate the least number of moves the user can finish the game in 
num_optimal_moves = (2 ** num_disks) - 1
print("\nThe fastest you can solve this game is in " + str(num_optimal_moves) + " moves.")

#Get User Input
def get_input():
  choices = []
  choices.append(left_stack.get_name()[0])
  choices.append(middle_stack.get_name()[0])
  choices.append(right_stack.get_name()[0])
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter " + letter + " for " + name)
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
    else:
      print("Please enter choice from the ones listed above.")
  
#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or (from_stack.peek() < to_stack.peek()):
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again.")
print("\n\nYou completed the game in " + num_user_moves + " moves, and the optimal number of moves is " + num_optimal_moves)
