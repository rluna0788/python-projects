# function multiplies two numbers without using multiplication operators - optimized to loop to smallest value
def multiplyByAddition(val1, val2):

    counter = 0
    sum = 0

    minNum = min(val1, val2)
    maxNum = max(val1, val2)

    while (counter < minNum):

        sum += maxNum
        counter += 1
    
    print(sum)
    
multiplyByAddition(2, 1000)