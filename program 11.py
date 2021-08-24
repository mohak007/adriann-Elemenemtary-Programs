#Write a program that computes the sum of an alternating series where each element of the series is an expression of the form ((-1)^{k+1})/(2 * k-1) for each value of k from 1 to a million, multiplied by 4. Or, in more mathematical notation
#4\cdot \sum_{k=1}^{10^6} \frac{(-1)^{k+1}}{2k-1} = 4\cdot(1-1/3+1/5-1/7+1/9-1/11\ldots).
# ((-1)^{k+1})/(2 * k-1)
a=10
for a in range(1,10):
    b =((-1)**(a+1))/(2 * a-1)
    print(f'the sum for value a:{a} is {b} ')
