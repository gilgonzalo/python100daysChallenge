# https://www.youtube.com/watch?v=fOFWkmAyCHY
# day 13 Challenge

# 2 decimal places

testName = input ("Name of your test\n")
testMaxGrade = int(input ("What is the max. possible score?\n"))
testGrade = float(input ("What was your test numeric grade?\n"))

calculatedScore=((testGrade/testMaxGrade))*100;
calculatedScore=round(calculatedScore,2)

print("Your score is ",calculatedScore)
if calculatedScore<=50:
    print("your letter grade is --> : U")
elif calculatedScore>50 and calculatedScore<=60:
    print("your letter grade is --> : D")
elif calculatedScore>60 and calculatedScore<=70:
    print("your letter grade is --> : C")
elif calculatedScore>70 and calculatedScore<=80:
    print("your letter grade is --> : B")
elif calculatedScore>80 and calculatedScore<=90:
    print("your letter grade is --> : A-")
elif calculatedScore>90 and calculatedScore<=100:
    print("your letter grade is --> : A+")
