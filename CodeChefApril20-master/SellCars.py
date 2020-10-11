'''
Chef owns N cars (numbered 1 through N). 
He wishes to sell all of them over N years by selling exactly one car per year. 
For each valid i, the initial price of the i-th car is Pi. Due to depreciation, 
the price of each car decreases by 1 unit per year until it is sold.
Note that the price of a car cannot drop below 0 no matter how many years have passed, 
i.e. when the price of a car reaches 0 in some year, 
it remains 0 in all subsequent years.

Find the maximum profit Chef can make if he sells his cars in an optimal way. 
Since this number may be large, compute it modulo 1,000,000,007 (109+7).
'''

# chef wants to Sell all the cars
import sys


def sell_cars():
    total_cars = int(sys.stdin.readline())
    price_list = list(sys.stdin.readline().split())
    # print(sorted(price_list))
    profit = 0
    price_list.sort(key=int, reverse=True)
    # print(price_list)
    for i in range(total_cars):
        cash = (int(price_list[i]) - i)
        # print(cash)
        if cash < 0:
            cash = 0
        profit = profit + cash
    print(profit % 1000000007)


T = int(sys.stdin.readline())
for t in range(T):
    sell_cars()  # To call the sell cars function T number of times
