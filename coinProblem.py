count = [0]

def change(goal, denominations, count):
    # base case
    if goal == 0:
        count[0] += 1
        return

    for coin in denominations:
        if len(denominations) == 1:
            if goal > coin and goal%coin == 0:
                count[0] += 1
            return
        i = 1
        while goal >= 0:
            change(goal, denominations[1:], count)
            goal = goal - (i * coin)
            i += 1


count = [0]
change(16, [10,5,1], count)

