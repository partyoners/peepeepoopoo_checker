
details = {
    "name": " ",
    "age" : " "
}

n = input("what is your name?")
a = input("what is your age?")

details.update({"name": n})
details.update({"age": a})

x = details.get("name")
a = details.get("age")

print(f"This is a peepeepoopoo check for {x}, age {a}")

#-------------------------

while True:
    
    z = input ("have you had a peepeepoopoo check? : ")

    #x = "complete, thank you"
    
    if z =="yes":
        print("you valid")
        break

    elif z =="no":
        print("check in progress")
        break

    else:
        print ("please enter yes or no")
        

print("check complete")

print(f"certificate of peepeepoopoo check for {x}, age {a}")            


     




