
def change(amount, denominations):
    # below: the index is the amount and the value
    # at each index is the number of ways
    # of getting that amount

    # initialize an array of zeros with indices
    # up to amount
    arrangement = [0] * (amount + 1)

    arrangement[0] = 1

    for coin in denominations:
        higher_amount = coin
        while higher_amount <= amount:
            remainder = higher_amount - coin
            print('higher amount is {}, coin is {}'.format(higher_amount, coin))
            print('remainder {}'.format(remainder))
            arrangement[higher_amount] += arrangement[remainder]
            higher_amount += 1
    return arrangement[amount]


amount = 4
denominations = [1,2,3]

print(change(amount, denominations))

def make_change(amount, denominations):
    # print "Amount :", amount, " Denominations:", denominations
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 0:
        return 0
    return make_change(amount-denominations[0], denominations) + \
        make_change(amount, denominations[1:])

# print(make_change(amount, denominations))