import random 

# so wecan add names
names = []

#if it is true the progres will countni normal and repet the progres of adding names to the list
while(True):
    answer = input("what name u want to add: ")
    # IF U INTER WITHOUT WRITHING ANY NAME IT WILL BRAK AND END
    if (answer == ""):
        break
    else:
        names.append(answer)

# We randomly choose one name from the list print it out and then remove it from the list and continue this for every name we have on the list
for i in range(len(names)):
    chosen = random.choice(names)
    print("number " + str(i+1) + " " + chosen)#A
    names.remove(chosen)