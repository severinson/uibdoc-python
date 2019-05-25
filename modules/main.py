import random
print(random.random())

import random as trulyrandom
print(trulyrandom.random())

from random import random
print(trulyrandom.random())

# amazing modules. such useful. much tools.
import itertools
import functools

from datetime import datetime, timedelta
today = datetime.today()
tomorrow = today + timedelta(days=1)
print(today, tomorrow)

# import submodule.usefulstuff
# v = submodule.usefulstuff.do_useful_work(1, 2)
# print(v)

import submodule
v = submodule.usefulstuff.do_useful_work(1, 2)
print(v)
