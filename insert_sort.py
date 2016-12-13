def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            else: break
def find_minimum(A):
    minimum = A[0]
    for element in A:
        if element < minimum:
            minimum = element
    return minimum
def loop0(n):
    for i in range(0, n):
        print(i)
def loop1(n):
    for i in range(0, n*n):
        print(i)
def loop2(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i,j)
def loop3(n):
    for i in range(0, n):
        for j in range(0, i):
            print(i,j)
def loop44(n):
    for i in range(0, n):
        for j in range(0, i*i):
            print(i,j)
def concatenate0(n):
    for i in range(n*n):
        print(i)
    for j in range(n*n*n):
        print(j)

def concatenate1(n):
    if a < 0:
        for i in range(n*n):
            print(i)
    else:
        for j in range(n*n*n):
            print(j)
import random
a=[random.randint(0, 100) for k in range(20)]
insertion_sort(a)
print(a)
