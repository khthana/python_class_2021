score = float(input("Enter score = "))

if (score % 1) >= 0.5:
      Before_point = score // 1
      score = Before_point + 1
      print("Round up score =", score)

if(score < 50):
      print("Your grade is 0.0")
elif (score >= 50 and score < 55):
      print("Your grade is 1.0")
elif (score >= 55 and score < 60):
      print("Your grade is 1.5")
elif (score >= 60 and score < 65):
      print("Your grade is 2.0")
elif (score >= 65 and score < 70):
      print("Your grade is 2.5")
elif (score >= 70 and score < 75):
      print("Your grade is 3.0")
elif (score >= 75 and score < 80):
      print("Your grade is 3.5")
elif (score >= 80):
      print("Your grade is 4.0")
else:
      print("Your score is incorrect")
