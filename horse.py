import random
import sys


with open('Viet11K.txt') as f:
    words = f.read().splitlines()
dwords = [w for w in words if len(w.split()) == 2 and len(w) < 11]
count = int(sys.argv[1]) if len(sys.argv) > 1 else 4

rand = random.SystemRandom()
print('.'.join(rand.choice(dwords) for _ in range(count)))
