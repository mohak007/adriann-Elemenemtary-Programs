#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
num=int(input("enter number :"))
print(num)
def sum ():
    if num % 3 == 0:
        sum = (num*(num+1))/2
        print(f"The sum is {sum} ")
    elif num%5==0:
        sum = (num * (num + 1)) / 2
        print(f"The sum is {sum} ")
    else :
        print("not a multiple of 3")
sum()