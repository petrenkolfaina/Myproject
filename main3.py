list = [0,0,1,4,4,-6,-2,-6,7]
i = list[-1]
for index, i in enumerate(list):
    if i < 0:
        print("The last negative num is ", i)
        print("Index is ", index)
        break
