A = 12001
B = 510
C = 7007
D = 6034
def minDifference(A):
    A = list(str(A))
    mn = float('inf')
    res = []
    for i in range(1, len(A)):
        firstPart = A[:i]
        secondPart = A[i:]
        while firstPart[0] == '0':
            if len(firstPart) == 1:
                break
            firstPart.pop(0)
        while secondPart[0] == '0':
            if len(secondPart) == 1:
                break
            secondPart.pop(0)
            

        firstNumber = ''.join(firstPart)
        secondNumber = ''.join(secondPart)
        absDifference = abs((int)(firstNumber) - (int)(secondNumber))
        res.append(absDifference)
        mn = min(mn, absDifference)
    return mn, res
print(minDifference(A))
print(minDifference(B))
print(minDifference(C))
print(minDifference(D))
