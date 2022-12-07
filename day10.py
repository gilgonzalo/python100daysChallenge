# https://www.youtube.com/watch?v=8pzLxVej3_g
# Little bit of math
#  addition
#  subtraction
#  multiplication
#  division
#  divisor

myBill = float (input("How much  was the bill?\n"))
numberOfPeople = int(input("Divided between how many people\n"))
percentageTip = int(input("What percentage of tip you want to give (0 for none)\n"))
subtotal = myBill / numberOfPeople
subtotal = round(subtotal,2)
tipAmount = subtotal * (percentageTip/100)
tipAmount = round(tipAmount,2)
totalBillTipIncluded = subtotal + tipAmount
totalBillTipIncluded = round(totalBillTipIncluded,2)

print("Sub total before tip for each: ",subtotal)
print("Tip value for each: ",tipAmount)
print("Total bill with the tip included for each : ",totalBillTipIncluded)





