print("Welcome to the quiz !")

play=input("Do you want to enter the battle field? ")
if play.lower() != "yes" :
    quit()

print("Okay,Lets play")
Score=0

answer=input("what does ilt stands for ?")
if answer.lower() == "i love you":
    print("Correct! ----------------")
    Score+=1
else:
    print("Incorrect! --------------")


answer=input("what does jk stands for ?")
if answer.lower() == "just kidding":
    print("Correct! ----------------")
    Score+=1
else:
    print("Incorrect! --------------")


answer=input("what does ihy stands for ?")
if answer.lower() == "i hate you":
    print("Correct! ----------------")
    Score+=1
else:
    print("Incorrect! --------------")

answer=input("what does lmao stands for ?")
if answer.lower() == "laughing my ass out":
    print("Correct! ----------------")
    Score+=1
else:
    print("Incorrect! --------------")


print("The Total points you scored out of 4 Questions is " + str(Score))
print("You scored" + str((Score/4)*100) + "%")
