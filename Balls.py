from random import *


class powerball:
    def winnum(self):
        self.winnumlist = []                                # get a list of 5 random ints between 1 and 20 (inclusive)
        for i in range(5):
            self.white_ball = randrange(1, 20)
            while self.white_ball in self.winnumlist:
                self.white_ball = randrange(1, 20)
            self.winnumlist.append(self.white_ball)
        self.winnumlist.sort()
        for j in range(1):
            self.powerball = randrange(1, 10)
            self.winnumlist.append(self.powerball)          # add 1 int to the list between 1 and 10
        return self.winnumlist

    def luckynum(self):
        self.luckynumlist = []                              # get a list of 5 random ints between 1 and 20 (inclusive)
        for i in range(5):
            self.white_ball = randrange(1, 20)
            while self.white_ball in self.luckynumlist:
                self.white_ball = randrange(1, 20)
            self.luckynumlist.append(self.white_ball)
        self.luckynumlist.sort()
        for j in range(1):
            self.powerball1 = randrange(1, 10)
            self.luckynumlist.append(self.powerball1)       # add 1 int between 1 and 10
        return self.luckynumlist