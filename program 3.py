#Modify the previous program such that only the users Alice and Bob are greeted with their names.
name=input("enter your name :")
def func():
    if name == "Alice" :
        print(f"Good Morning {name}")
    elif name == "BOB":
        print(f"Good Morning {name}")
    else :
        print("Wrong input")

func()