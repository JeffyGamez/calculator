import time 
import random
import math
print ("This repo was made by jeffygamez")
print ("now loading")
time.sleep (5)
print ("Welcome To Random Joke Generator version 1.3.2")
joke_1 = "Why did the chicken cross the road? To run from the KFC"
joke_2 = "Have you heard the rumor of the margarin? Never mind I butter not spread it"
joke_3 = "What did the eraser say to the pencil? You're lookin mighty sharp today"

keep_playing = "yes"

while keep_playing == "yes" or keep_playing == "Yes":
  joke_selected = random.randint (1, 3) 

  print (f"Selecting Random Joke Number: {joke_selected}")

  time.sleep (3)

  if joke_selected == 1:
    print (f"Random Joke Is: {joke_1}")

    elif joke_selected == 2:
      print (f"Random Joke Is: {joke_2}")

    elif joke_selected == 3:
      print (f"Random Joke Is: {joke_3}")
   
  valid_input = False 
  while valid_input == False:
    
    keep_playing = input ("Would You Like To Keep Playing Yes/No")
  
    if keep_playing == "Yes" or keep_playing == "yes":
      valid_input = True
      continue
    elif keep_playing == "No" or keep_playing == "no":
      print ("Goodbye Thank You For Using Random Joke Generator Version 1.3 By JeffyGamez")
      valid input = True
      break
    else:
      print ("ERROR, Invalid Input!")
      
  



