import random
what = input("Is this a Hello World program to understand Git: ")
randomize = ["yes","no","hello","word",]

if what.lower() == "randomize":
    what = random.choice(randomize)
    print(what)

if what.lower() == "yes":
    print("No, that was last week")
elif what.lower() == "no":
    print("Correct, this program is a merge conflict example")
elif what.lower() == "hello" or what.lower() == "hello world" or what.lower() == "hello world!!!":
    print("Hello World!!!")
elif what.lower() == "word1" or what.lower() == "word2" or what.lower() == "word3": #Merge Conflict word
    print("Funny")
else:
    pass