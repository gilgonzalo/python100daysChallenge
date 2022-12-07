# https://www.youtube.com/watch?v=4hNQsFN9ki8
# Casting
# int
# float

userYear= int( input ("What year were you born in (4 digits please) :\n"))
if userYear > 2012 and userYear <= 2023:
    print("Hello generation Alpha, I am surprised you can even type")
elif userYear >= 1997 and userYear <= 2012:
    print("Hellotus my Gen-Z person!")
elif userYear >= 1981 and userYear <= 1996:
    print("I am a Millenial just as much as you are (but that's our little secret)")
elif userYear >= 1965 and userYear <= 1980:
    print("Generation X, it reminds me of the X files")
elif userYear >= 1946 and userYear <= 1964:
    print("Baby Boomer, I bet you're not that much of a baby anymore")
elif userYear >= 1928 and userYear <= 1945:
    print("Silent Generation, I actually didn't know the name of your generation until now")
elif userYear >= 1901 and userYear <= 1927:
    print("Greatest generation, I really wonder if is really called like that and why")
elif userYear >= 1883 and userYear <= 1900:
    print("OMG, you're from the Lost Generation, I hardly believe you're actually alive anymore, according to me the oldest person alive is les than 122 yearls old")
else:
    print("So, you're either a baby or a Vampire (or Namor)")

