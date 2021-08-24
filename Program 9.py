#Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

number=int(input("enter the number:"))
print(number)
for i in range(1,10):
    num = int(input("enter the number:"))
    print("the num is :", num)
    if number == num:
        print("both num and number is same")
        print(f"number of tries done :{i}")
        j = 10
        print(f"number of tries left :{j - i}")
    elif len(str(number))>5:
        print("the number is large ")
    else :
        print("The number is small")
        break
print(f"number of tries done :{i}")
j=10
print(f"number of tries left :{j-i}")



