# https://www.youtube.com/watch?v=cuseM3bReT4
# Day 16 - While true loop

print("Complete the lyrics\n")
counter = 0
while True:
    counter+=1
    print("You will be guessing part of the lyrics of one of my favourites songs\n")
    lyrics=input("Lloro, por quererte, por amarte y por ________\n")
    if lyrics=="desearte" or lyrics=="Desearte" or lyrics=="DESEARTE" or lyrics=="dESEARTE":
        break
    print("Keept trying\n")
if counter == 1:
    print("Great, you made it on your first shot")
elif counter >= 2 and counter <=3:
    print("Not so bad, it took you",counter,"times")
elif counter >= 4 and counter <=5:
    print("mmmmm, just took",counter,"times")
elif counter >= 6:
    print("You need to step up your game. Seriosly?",counter,"times!!!")
    



    
