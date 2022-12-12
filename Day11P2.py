import time
import math
from operator import mod
st = time.time()

items = [[96, 60, 68, 91, 83, 57, 85],[75, 78, 68, 81, 73, 99],[69, 86, 67, 55, 96, 69, 94, 85],[88, 75, 74, 98, 80],[82],[72, 92, 92],[74, 61],[76, 86, 83, 55]]
opperation = [['*',2],['+',3],['+',6],['+',5],['+',8],['*',5],['**',2],['+',4]]
test = [[17,2,5],[13,7,4],[19,6,5],[7,7,1],[11,0,2],[3,6,3],[2,3,1],[5,4,0]]
busy = [0,0,0,0,0,0,0,0]
lcm = math.lcm(17,13,19,7,11,3,2,5)

for x in range (1,10001):
    for i in range(0,8):
        pops = 0
        for item in items[i]:
            opperator, val = opperation[i]
            match opperator:
                case '*':
                    item = item * val
                case '+':
                    item = item + val
                case '**':
                    item = item ** val
            item = mod(item, lcm)
            if item % test[i][0] == 0:
                items[test[i][1]].append(item)
            else:
                items[test[i][2]].append(item)
            busy[i] += 1
            pops += 1

        items[i] = items[i][:-pops or None]

busy_max_1 = max(busy)
busy.remove(busy_max_1)
busy_max_2 = max(busy)
print('Max 1(' + str(busy_max_1) + ') * Max 2(' + str(busy_max_2) + ') = ' + str(busy_max_1 * busy_max_2))

et = time.time()

# get the execution time
elapsed_time = et - st
final_res = elapsed_time * 1000
print('Execution time:', final_res, 'ms')