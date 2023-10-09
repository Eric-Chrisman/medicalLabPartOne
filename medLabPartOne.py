print("Hello, this program will take inputs of your vitals in order to check your health.\n")
age = int(input("Enter your age (whole numbers olny):\n"))
print()

if age < 17:
  print("You are too young for this program. If you have a need for a medical checkup, go see your pediatrician")
else:
  eplison = 0.000001   #float comparison value
  temperature = 0.0    #fahrenheit
  vitaminCLevel = 0.0  #mg/dL
  sex = False          #True = male; False = female (defalut)
  height = 0.0         #inches
  MALE_AVG = 69        #Male avg
  FEMALE_AVG = 64      #female avg
  tempAvg = FEMALE_AVG #temp avg (female defalut)

  #temperature check
  temperature = float(input("Enter your temperature in Fahrenheit:\n"))
  if temperature > 100:
    print("Your temperature is too high")
  elif temperature < 95:
    print("Your temperature is too low")
  elif abs(temperature - 98.6) < eplison:
    print("Your temperature is textbook perfect")
  else:
    print("Your temperature is good")
  print()

  #vitamin C check
  vitaminCLevel = float(input("Enter your vitamin C level (mg/dL):\n"))
  if vitaminCLevel > 1.5:
    print("Your vitamin C level is dangerously high")
  elif abs(vitaminCLevel - 1.5) < eplison:
    print("It's dangerous for your vitamin C level to go any higher")
  elif vitaminCLevel < 0.4:
    print("Your vitamin C level is dangerously low")
  elif abs(vitaminCLevel - 0.4) < eplison:
    print("It's dangerous for your vitamin C level to go any lower")
  else:
    print("Your vitamin C level is good")
  print()
  
  #height check
  # temp storage of inputed sex, then is changed to be a standin for a word during height comparsion
  genderVerb = input("Enter your gender (m for male; f for female):\n")
  if(genderVerb == "m" or genderVerb == "M"):
    genderVerb = "man"
    sex = True
    tempAvg = MALE_AVG
  else:
    genderVerb = "woman"
    #sex is female by deafult
  print()

  height = int(input("Enter you total height as a whole number in inches:\n"))
  if abs(height - tempAvg) < eplison:
    print("Your height is equal to the average height for your gender")
  elif height > tempAvg:
    print(f"You are {height - tempAvg} inches taller than your average {genderVerb}")
  else:
    print(f"You are {tempAvg - height} inches shorter than your average {genderVerb}")

print("\nProgram finished")
  
