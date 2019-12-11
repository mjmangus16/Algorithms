#!/usr/bin/python

import argparse


def find_max_profit(prices):

    cur_max = -5000

    for index, b in enumerate(prices):
        for s in range(index+1, len(prices)):

            if prices[s] - b > cur_max:
                cur_max = prices[s] - b

    return cur_max


print(find_max_profit([32, 16, 8, 4, 2]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
