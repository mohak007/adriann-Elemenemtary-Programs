#Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)
num=int(input("enter the value"))
def prime():
    for i in range(2,num):
        if num % i == 0:
             print(f"the {num} is  not prime")
             break
    else:
        print(f"the {num} is prime")

prime()