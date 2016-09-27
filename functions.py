def hello(name):
    print "Hello %r" % (name)

hello("Matt")

import matplotlib.pyplot as plot
import math
from numpy import arange

# def f(x):
#     return x + 1
#
# xs = range(-3, 4)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs, ys)
# plot.show()

# def f(x):
#     return x * x
#
# xs = range(-100, 101)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs, ys)
# plot.show()

# def f(x):
#     if x % 2 == 0:
#         return -1
#     else:
#         return 1
#
# xs = range(-5, 6)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.bar(xs, ys)
# plot.show()

# def f(x):
#     return math.sin(x)
#
# xs = arange(-5, 6, 0.1)
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs, ys)
# plot.show()

# def tempConvert(x):
#     return x * 1.8 + 32
#
# xs = arange(-100, 100)
# ys = []
# for x in xs:
#     ys.append(tempConvert(x))
#
# plot.plot(xs, ys)
# plot.show()

def playAgain():
    play = str.upper(raw_input("Do you wanna play again (Y or N)? "))
    while play != "Y" and play != "N":
        print "Invalid input"
        play = str.upper(raw_input("Sorry, could you retype your Y or N? "))
    if play == "Y":
        return True
    else:
        return False

print playAgain()
