print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("ok! Lets play ;)")
score = 0  

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")  

answer = input("what does GPU stand for? ")
if answer == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!") 

answer = input("what does RAM stand for? ")
if answer == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect!") 

print(" You got" + str(score) + "questions correct!") 
print(" You got" + str((score / 3) * 100) + "%.") 
