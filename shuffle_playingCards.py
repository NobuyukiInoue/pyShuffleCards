import os
import sys
import time
from typing import List, Dict, Tuple

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        exit_msg(argv[0])

    if argv[1].isnumeric() == False:
        print("{0} is not numeric.".format(argv[1]))
        exit(1)

    n = int(argv[1])
    if not 0 <= n <= 2:
        print("The number of jokers is either 0, 1, or 2.".format(argv[1]))
        exit(1)

    cards = Cards(n)
    time0 = time.time()
    res = cards.repeat_shuffle()
    time1 = time.time()

    print("{0}th ... next_cards is the same as first_cards.".format(res))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

def exit_msg(argv0: str) -> None:
    print("Usage: python {0} <Number of Jokers (0-2)>".format(argv0))
    exit(0)

class Cards:
    def __init__(self, number_of_Jokers: int) -> None:
        self.cards = []
        for suit in "SHDC":
            for i in range(1, 11):
                self.cards.append(suit + str(i))
            self.cards.append(suit + "J")
            self.cards.append(suit + "Q")
            self.cards.append(suit + "K")
        for i in range(number_of_Jokers):
            self.cards.append("Joker" + str(i + 1))

    def repeat_shuffle(self) -> int:
        print("The number of cards is {0}".format(len(self.cards)))
        print("0th...{1}\n".format(0, self.cards))

        next_cards = self.cards
        i = 1
        while True:
          # print("{0} times shuffled.".format(i))
            next_cards = self.perfect_shuffle(next_cards)
            print("{0}th...{1}".format(i, next_cards))
            if next_cards == self.cards:
                return i
            i += 1

    def perfect_shuffle(self, arr: List[str]) -> List[str]:
        arr_len = len(arr)
        N = arr_len//2
        ret = [""]*arr_len
        for i in range(N):
            ret[2*i] = arr[i]
        for i in range(N, 2*N):
            ret[2*i - 2*N + 1] = arr[i]
        if len(arr) % 2 == 1:
            ret[arr_len - 1] = arr[arr_len - 1]
        return ret

if __name__ == "__main__":
    main()
