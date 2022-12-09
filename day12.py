# https://www.youtube.com/watch?v=MHY4Ei2U60k
# DAY 12 - Debug my code! 

print("""100 Days of Code QUIZ

    How many can you answer correctly?""")
ans1 = input("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = int(input("Which lesson number is this?"))
if ans2>12:
    print("We're not quite that far yet")
elif ans2==12:
    print("That's right!")
else:
    print("We've gone well past that!")