import os, sys
stats = os.stat(sys.argv[1])
print(stats.st_size)