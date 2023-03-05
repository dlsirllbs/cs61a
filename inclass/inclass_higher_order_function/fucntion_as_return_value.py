from operator import add
def make_adder(n):
    #Return a function that takes one argument k and retrun k+n
    def adder(k):
        return k + n
    return adder