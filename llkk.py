name = input("What's your name?")
file = open("myTextFile.txt", "w")
file.write(name)
file.close()