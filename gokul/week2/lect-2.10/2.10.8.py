# simulate a coin toss, if the random number generated is >0.5 , print 'heads' else 'tails'

import random

num = random.random()
if num > 0.5 :
    print('heads')
else:
    print('tails')