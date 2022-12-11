# https://www.youtube.com/watch?v=Abk1jPdnMIc
# Nesting

print("This Hyper sofisticated system to detect if in fact you really are Gonzalo")

favMovie = input("Gonzalo, What's is your favourite movie\n")
impostorMessage = "You are no Gonzalo, and you will never be"
selfMessage = "Welcome Gonzalo AKA Chuyuyuyy"

if favMovie =="Matrix" or favMovie =="matrix":
    favOfAll = input("Which one of the Four is your favourite one (type it with letter)\n")
    if favOfAll == "One" or  favOfAll == "one" or favOfAll == "1":
        poster = input("You had some poster of one of the movies, which movie was\n")
        if poster == "Two" or  poster == "two" or poster == "2":
            mainCharacter = input("you have a funko of neo from which movie\n")
            if mainCharacter == "Four" or  mainCharacter == "four" or mainCharacter == "4":
                print(selfMessage)
            else:
                print(impostorMessage)
        else:
            print(impostorMessage)
    else:
        print(impostorMessage)
elif favMovie =="Kill Bill" or favMovie =="Kill bill" or favMovie =="kill bill":
    favOfAll = input("Which one of the Two is your favourite one (type it with letter)\n")
    if favOfAll == "Two" or  favOfAll == "two" or favOfAll == "2":
        nameCharacter = input("What's the name of the Bride\n")
        if nameCharacter == "Kiddo" or nameCharacter == "kiddo" or nameCharacter == "Beatrix":
            dialogMovie = input("Complete this dialog from spanish in the movie --> Despedacen a la....\n")
            if dialogMovie == "Perra" or dialogMovie == "perra":
                print(selfMessage)
            else:
                print(impostorMessage)
        else:
            print(impostorMessage)
    else:
        print(impostorMessage)
elif favMovie =="EEAAO" or favMovie =="eeaao" or favMovie =="Eeaao" or favMovie =="Everything, everywhere at all once" or favMovie =="Everything everywhere at all once\n":
    laughedHysterical = input("Is it true you lauhged the most hysterical at the cinema with that movie (yes/no)\n")
    if (laughedHysterical == "Yes" or laughedHysterical == "yes" or laughedHysterical == "True" or laughedHysterical == "true" or laughedHysterical == "y" or laughedHysterical == "Y"):
        circularObject = input("What's the object that is represented by a circle\n")
        if (circularObject == "Bagel" or circularObject == "bagel"):
            atTheEnd = input("at the end: ")
            if (atTheEnd == "Nothing really matters" or atTheEnd == "nothing really matters"):
                print(selfMessage)
            else:
                print(impostorMessage)
        else:
            print(impostorMessage)
    else:
        print(impostorMessage)
else:
    print(impostorMessage)