
# Have the computer choose a random number 
import random
cpt_number=random.randint(1,10)
#print("The computer's number is:" + str(cpt_number))


# Prompt the user to guess and store their guess in a variable 

user_number=int(input("What is the user's number: "))
#print("The user's number is:" + str(user_number))
'''
# Conditional statements to compare the two numbers
#player got it
if(cpt_number==user_number): 
  print("You got it! Computer's number is " + str(cpt_number) + " and your number is " + str(user_number))
  
#player number too low
elif(cpt_number>user_number):
  print("Your number is too low. Computer's number is " + str(cpt_number) + " and your number is " + str(user_number))

#player number too high
else:
  print("Your number is too high. Computer's number is " + str(cpt_number) + " and your number is " + str(user_number))
'''


#while(cpt_number>user_number or cpt_number<user_number):
while(cpt_number != user_number):
    if(cpt_number>user_number):
      print("Your number is too low.")
    if(cpt_number<user_number):
      print("Sorry you're number is too high.")
    user_number=int(input("What is your number: "))
    #if(cpt_number==user_number):
     # print("Yay you have won")
else:
  print("Yay you've won")