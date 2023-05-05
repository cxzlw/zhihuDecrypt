import os

dicts = {}

for filename in os.listdir("dicts"):
    if filename == "charset.txt":
        with open("dicts/" + filename, "r") as f:
            charset = f.read()
        continue
    with open("dicts/" + filename, "r") as f:
        dicts[filename.rstrip(".txt")] = f.read()
