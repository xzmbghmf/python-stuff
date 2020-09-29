print("A cup of tea 🍵")
print("Welcome to my tea shop! We have the finest selection of tea for (almost) every mood!")
print("Please input 'I'm fine' if you don't need help for the time being!")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  tea_list = []
  cure_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day")
      tea_list.append("green tea")
      cure_list.append("make yourself feel better")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      tea_list.append("white tea")
      cure_list.append("relax and enjoy the moment")
      counter -= 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think")
      tea_list.append("masala tea")
      cure_list.append("give yourself an energy boost")
      counter += 1
    if each_word == "fine":
      feelings_list.append("fine")
      encouragement_list.append("you should sttay positive!")
      tea_list.append("of our finest teas")
      cure_list.append("help you feel better the next time you come")
      counter -= 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". Do remember that "+ encouragement_list[0] + "! Hope you feel better :) Why not drink some "+ tea_list[0] + " to " + cure_list[0] + "?"

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += encouragement_list[-1]
    
    tea = ""
    for y in range(len(tea_list)-1):
      tea += tea_list[i] + ", "
    tea += tea_list[-1]
    
    cure = ""
    for x in range(len(cure_list)-1):
      cure += cure_list[i] + ", "
    cure += cure_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Also, you can drink some " + tea + " to " + cure + "! Have a nice day! :)"

  print()
  print(output)
  print()
