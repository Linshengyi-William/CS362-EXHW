def findSum(lis,targetSum):
    for i in range(len(lis)):
        for j in range(len(lis)):
            nextNum = 0
            if j+1 > len(lis)-1:
                nextNum = lis[0]
            else:
                nextNum = lis[j+1]
            if int(lis[i]) + int(nextNum) == targetSum:
                newLis = [lis[i],nextNum]
                return newLis
    return False

def printArray(lis):
    for i in range(len(lis)):
        print(lis[i],end= ' ')
    print("\n")

        


inputLis = input("Please enter an list of a number, speate each number by add an space between them: ")
targetSum = int(input("Please enter the target sum: "))

lis = inputLis.split(" ")

print("Number List you entered: ")
printArray(lis)
print("Result: ")
if findSum(lis, targetSum) != False:
    printArray(findSum(lis, targetSum))
else:
    print("We couldn't find the target sum from the list you entered")


