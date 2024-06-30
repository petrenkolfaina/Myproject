list = [1,2,3,4,5,6,-6,-5,-4,-3,-2,-1,132,456,0,0,1,4,4,-6,2,6,-7]
for index, i in enumerate(list):
    if i < 0:
        print("First negetive number is ",i)
        print("Index is ", index)
        break

