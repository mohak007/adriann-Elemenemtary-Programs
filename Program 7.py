#Write a program that prints a multiplication table for numbers up to 12.

num=int(input("Enter the number :"))
def func():
    for i in range(1,11):
        result=num*i
        print(f"{num} * {i} = {result}")
func()