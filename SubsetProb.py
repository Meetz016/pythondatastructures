def findSubset(l, i, tar, curr,temp):
    if i >= len(l):
        return
    if sum(temp) == tar:
        print(temp)
        return
    #take

    #skip


l = [1,2,1,4]
findSubset(l, 0, 4,l[0],[])
