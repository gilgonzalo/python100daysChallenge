
# https://www.youtube.com/watch?v=AwCI7IG-i38
# Day 15 - Loops

print("ONOMATOPEYApedia? ")
continuar='Y'
while continuar=='Yes' or continuar=='YEs' or continuar=='yes' or continuar=='y' or continuar=='Y':
    animal=input("What animal onomatopeya do you want to know?\n")
    if animal=="cow" or animal=="Cow" or animal=="COW":
        print("Vaca onomatopeya sounds ===> 🐮 MUUUUUUUU")
    elif animal=="dog" or animal=="Dog" or animal=="DOG":
        print("Dog onomatopeya sounds ===> 🐶 WAUUU WAUUU")
    elif animal=="cat" or animal=="Cat" or animal=="CAT":
        print("Cat onomatopeya sounds ===> 🐱 MIAUUUUUU")
    elif animal=="penguin" or animal=="Penguin" or animal=="PENGUIN":
        print("Penguin onomatopeya sounds ===> 🐧 MEKMEKMEK")
    elif animal=="monkey" or animal=="Monkey" or animal=="MONKEY":
        print("Monkey onomatopeya sounds ===> 🙊 UUHHHAAAUAHUHH")
    elif animal=="dolphin" or animal=="Dolphin" or animal=="DOLPHIN":
        print("Dolphin onomatopeya sounds ===> 🐬 IHHHIHHHIHHH")
    else:
        print("That animal has not been added to the DB ===> Error 503")
    continuar=input("Do you to know more Onomatopeyas (y/n)? ")

