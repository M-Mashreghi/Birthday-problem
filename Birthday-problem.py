import math
import matplotlib.pyplot as plt

def _function_(n, k):
    answer = (1-(math.factorial(n))/ ((math.factorial(n-k))* n**k))
    return answer


a = ["A", "a", "1"]
b = ["B", "b", "2"]
c = ["C", "c", "3"]

n = 0
k = 0

option = input("Hi \npls enter what section do u wanna go?\nA:23 people and 365 days\nB:enter the number of people and days you want \nC: the graph of probibilety from 1 to 80 people and 365 day\nanswer:")

if option == a[2] or option == a[1] or option == a[0]:  # part A
    print(_function_(365, 23))
elif option == b[2] or option == b[1] or option == b[0]:  # part B
    n = int(input("pls enter how many days u want?"))
    k = int(input("pls enter how many people are there?"))
    if k <= 0 or n <= 0:
        print("I can't accept negative numbers\npls try again")  # check Entries
        exit()
    if k >= n:
        print("the answer is 1 without calculating ")  # check Entries
        exit()
    if 1 >= k:
        print("the answer is 0 without calculating ")  # check Entries
        exit()
    print(_function_(n, k))
elif option == c[2] or option == c[1] or option == c[0]:  # part C

    k = [1, 2]
    probability = [0, 1 / 365]
    for i in range(3, 80 + 1):  # calculation
        n = 365
        k.append(i)
        probability.append(_function_(n, i))

    # ploting part
    plt.plot(k, probability, color='b', linewidth='2.5')
    plt.xlabel('amount of k')
    plt.ylabel('amount of posilibity')
    plt.title('possibility of two people were born in 1 day')
    plt.show()

else:
    print("ur order not found")




