import random
words = ["Python","Name","Ring","Class","Orange","Java","Water","Ring","Fly","Magic","Wheel","Java","Card","Economy","Computer","Python"]

#Step-1: 
for i in range(1,6):
  random_number = random.randint(2,3)
  
  random_words = random.sample(words,random_number)
  #print(random_words)
  # Water-Java
  # Water_Java 
  # Water Java
  #Water$Java
  #Step-2: 
  random_string = "".join(random_words)
  print(f"{i}. {random_string}")


