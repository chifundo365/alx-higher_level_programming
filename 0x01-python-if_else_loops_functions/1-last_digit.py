#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
last = int(last)
msg = 'Last digit of {} is {}'.format(number, last)
if number < 0:
    msg = 'Last digit of {} is -{}'.format(number, last)
    print("{} and is less than 6 and not 0".format(msg))
elif last > 5:
    print("{} and is greater than 5".format(msg))
elif last < 6 and last != 0:
    print("{} and is less than 6 and not 0".format(msg))
else:
    print("{} and is 0".format(msg))
