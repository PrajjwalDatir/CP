'''
There are a total of N spots (numbered 1 through N)
where people can stand in front of the local shop. 
The distance between each pair of adjacent spots is 1 foot.
Each spot may be either empty or occupied; you are given a sequence A1,A2,…,AN, 
where for each valid i, Ai=0 means that the i-th spot is empty, while Ai=1 means that
there is a person standing at this spot. 
It is guaranteed that the queue is not completely empty.
For example, if N=11 and the sequence A is (0,1,0,0,0,0,0,1,0,0,1), 
then this is a queue in which people are not following the advice 
because there are two people at a distance of just 3 feet from each other.
You need to determine whether the people outside the local shop are 
following the social distancing advice or not. 
As long as some two people are standing at a distance smaller than 6 feet from each other,
it is bad and you should report it,
since social distancing is not being followed.
'''

testCases = int(input())
totalPeople = []
Queue = []

for i in range(testCases):
    Legal = 6
    temp = int(input())
    totalPeople = (input().split())
    result = "YES"

    for j in totalPeople:
        #print(totalPeople[i])
        #print(i)
        j = int(j)
        if j == 1 and Legal >= 6:
            Legal = 1
            continue
        elif j == 1 and Legal < 6:
            result = "NO"
            break
        elif j == 0:
            Legal = Legal + 1
            continue
    if result == "NO":
        print(result)
    else:
        print(result)
