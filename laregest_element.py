
#second largest number
def secondlargest(a, n):
    if n < 2:
        return -1
    firstlargest = a[0]
    secondlargest = -1
    for i in range (1,n):
        if firstlargest < a[i]:
            secondlargest = firstlargest
            firstlargest = a[i]
        elif secondlargest < a[i]:
            secondlargest = a[i]
    return secondlargest

arr = [2,4,1,3,5]
num = 5
seclargest =  secondlargest(arr,num)
print(seclargest)



# Third largest number
def thirdlargest(a, n):
    if n < 3:
        return -1
    firstlargest = a[0]
    secondlargest = -1
    thirdlargest = -1   
    for i in range (1,n):
        if firstlargest < a[i]:
            thirdlargest = secondlargest
            secondlargest = firstlargest
            firstlargest = a[i]
        elif secondlargest < a[i]:
            thirdlargest = secondlargest
            secondlargest = a[i]
        elif thirdlargest < a[i]:
            thirdlargest = a[i]
    return thirdlargest

largest = thirdlargest(arr,num)
print(largest)