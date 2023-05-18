import os

words = dict()
dicts = dict()

path = os.path.dirname(__file__)

with open(path + "/words.txt", "r") as f:
    words_text = f.read()
    words["none"] = dict(map(lambda x: (x.split(" ")[0], int(x.split(" ")[1])),
                             words_text.rstrip("\n").split("\n")))

with open(path + "/dicts/charset.txt", "r") as f:
    charset = f.read()

for filename in os.listdir(path + "/dicts"):
    if filename == "charset.txt":
        continue
    with open(path + "/dicts/" + filename, "r") as f:
        encrypt_method = filename.rstrip(".txt")
        dicts[encrypt_method] = f.read()
        # words[encrypt_method] = set(words_text.translate(str.maketrans(dicts[encrypt_method], charset)).split("\n"))
        # words[encrypt_method] = list(words_text.translate(str.maketrans(dicts[encrypt_method], charset)).split("\n"))
        words[encrypt_method] = dict(map(lambda x: (x.split(" ")[0], int(x.split(" ")[1])),
                                         words_text.translate(str.maketrans(dicts[encrypt_method], charset)).rstrip(
                                             "\n").split("\n")))
