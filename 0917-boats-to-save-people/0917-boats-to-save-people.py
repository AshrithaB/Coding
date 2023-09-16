'''
hashmap -> {weight:nop}
for i to n:
    if limit - w in hashmap:
        remove from hashmap
        inc boats
    else:
        add weight to hashmap
for k,v in hashmap:
    boats += v
return boats

3, 2, 2, 1
hashmap
0 : 1
2 : 1

boats = 1+1+1 = 3

3 1 1 1
hashmap
0 : 1
2 : 1

boat = 1+1+1

3 1 1 1 1


3 5 3 4
3 : 1


b = 1+1+1+1

3 3 4 5
i
  

3 2 2 1
1 2 2 3
j i

b = 1+1+1

people.sort()
i = 0
j = n-1
while j > 0:
    if people[j] == limit:
        b += 1
        j -= 1 
while i <= j:
    if people[i] + people[j] <= limit:
        b += 1
        i += 1
        j -= 1
    else:
        b += 1
        j -= 1
return b

'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        i = 0
        j = len(people)-1
        while j > 0 and people[j] == limit:
            j -= 1
            boat += 1
        while i <= j:
            if people[i] + people[j] <= limit:
                boat += 1
                i += 1
                j -= 1
            else:
                boat += 1
                j -= 1
        return boat
        