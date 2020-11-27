#O(N)
def moveZeros(num):
    j = 0
    for i in range(len(num)):
        if num[i] != 0:
            num[j] = num[i]
            j += 1
            if i != j:
                num[i] = 0
    return num

print(moveZeros([0,1,0,3,12]))



