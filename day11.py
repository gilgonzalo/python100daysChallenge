# https://www.youtube.com/watch?v=pKRE-W9HGNs
# day 11 challenge
# how many seconds in a year

print("We are calculating how many seconds a particular year contains ")
year = int(input("What year are you calculating?\n"))
leapOrNot=year % 4
if leapOrNot == 0:
    seconds=60*60*24*365
    print("Seconds per ",year," are : ",seconds)
elif  leapOrNot > 0:
    seconds=60*60*24*366
    print("Seconds per ",year," are : ",seconds)
