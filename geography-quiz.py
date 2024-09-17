print()
print("Geography Quiz")
print()

attempt = 1
score = 0

while True:
  question_one = input("1) Which country's flag features a maple leaf?\na) Canada\nb) Austrialia\nc) Germany\nd) Brazil\n ")
  if question_one.lower() == "a":
    print("Correct")
    score += 1
  elif question_one.lower() == "b":
    print("Incorrect")
  elif question_one.lower() == "c":
    print("Incorrect")
  elif question_one.lower() == "d":
    print("Incorrect")

  question_two = input("2) What is the only country that does not have a rectangular or square flag?\na) Switzerland\nb) Nepal\nc) Japan\nd) Bhuthan\n ")
  if question_two.lower() == "a":
    print("Incorrect") 
  elif question_two.lower() == "b":
    print("Correct")
    score += 1  
  elif question_two.lower() == "c":
    print("Incorrect")
  elif question_two.lower() == "d":
    print("Incorrect")

  question_three = input("3) Which country has the most official languages?\na) India\nb) Switzerland\nc) South Afirca\nd) Zimbabwe\n ")
  if question_three.lower() == "a":
    print("Incorrect")
  elif question_three.lower() == "b":
    print("Incorrect")
  elif question_three.lower() == "c":
    print("Incorrect")
  elif question_three.lower() == "d":
    print("Correct")
    score += 1
    
  question_four = input("4) The Union Jack is a combination of which countries’ flags?\na) England, Scotland, Ireland \nb) Wales, Scotland, England\nc) Ireland, Wales, Scotland\nd) England, Northern Ireland, Scotland\n ")
  if question_four.lower() == "a":
    print("Correct")
    score += 1
  elif question_four.lower() == "b":
    print("Incorrect")
  elif question_four.lower() == "c":
    print("Incorrect")
  elif question_four.lower() == "d":
    print("Incorrect")

  question_five = input("5) Which flag has a dragon on it?\na) Bhutan\nb) Wales\nc) China\nd) Denmark\n ")
  if question_five.lower() == "a":
    print("Incorrect")
  elif question_five.lower() == "b":
    print("Correct")
    score += 1
  elif question_five.lower() == "c":
    print("Incorrect")
  elif question_five.lower() == "d":
    print("Incorrect")

  question_six = input("6) What is the most widely spoken language in the world?\na) Spanish\nb) Mandarin\nc) English\nd) Hindi\n ")
  if question_six.lower() == "a":
    print("Incorrect")
    score += 1
  elif question_six.lower() == "b":
    print("Correct")
    score += 1
  elif question_six.lower() == "c":
    print("Incorrect") 
  elif question_six.lower() == "d":
    print("Incorrect")

  question_seven = input("7) Which country's flag has an eagle and a snake in its center?\na) Mexico\nb) Egypt\nc) Indonesia\nd) Turkey\n ")
  if question_seven.lower() == "a":
    print("Correct")
    score += 1
  elif question_seven.lower() == "b":
    print("Incorrect") 
  elif question_seven.lower() == "c":
    print("Incorrect")
  elif question_seven.lower() == "d":
    print("Incorrect")

  question_eight = input("8) Which continent has the most countries?\na) Europe\nb) Asia\nc) Afica\nd) South America\n ")
  if question_eight.lower() == "a":
    print("Incorrect")
  elif question_eight.lower() == "b":
    print("Incorrect") 
  elif question_eight.lower() == "c":
    print("Correct")
    score += 1
  elif question_eight.lower() == "d":
    print("Incorrect")

  question_nine = input("9) In which country is Mount Kilimanjaro located?\na) Kenya\nb) Tanzania\nc) Ethopia\nd) Uganda\n ")
  if question_nine.lower() == "a":
    print("Incorrect")
  elif question_nine.lower() == "b":
    print("Correct")
    score += 1
  elif question_nine.lower() == "c":
    print("Incorrect")
  elif question_nine.lower() == "d":
    print("Incorrect")

  question_ten = input("10) Which country has the oldest continuously used national flag?\na) Denmark\nb) Greece\nc) Japan\nd) France\n ")
  if question_ten.lower() == "a":
    print("Correct")
    score += 1
  elif question_ten.lower() == "b":
    print("Incorrect")
  elif question_ten.lower() == "c":
    print("Incorrect") 
  elif question_ten.lower() == "d":
    print("Incorrect")

  print()
  print(f"You got {score} / 10 ")
  print()

  print()
  again = input("Do you want to try again? ")
  print()
  if again.lower() == "no":
    break