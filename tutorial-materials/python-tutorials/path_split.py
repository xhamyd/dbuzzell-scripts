import os

path = os.environ["PATH"]
for f in path.split(":"):
    print(f)
