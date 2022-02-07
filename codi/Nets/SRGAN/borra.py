import sys

for n in range(100):
    print("\r%d   " % (100-n), end="")
    sys.stdout.flush()