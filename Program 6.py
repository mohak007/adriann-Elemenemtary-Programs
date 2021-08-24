#Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

num=int(input("Enter the  number :"))
print(num)
input=input("Enter your choice:")
print(f"your choice is :{input}")
def func():
    if input == "sum":
        summation = (num * (num + 1)) / 2
        print(f"The sum is {summation} ")
    elif input == "Product":
        p=num*(num-1)
        print(f"The product is {p}")
func()