from utils import *

c = get_cdycc(5899)
print("got")
print(decrypt(c, detect_encrypt_method(c)))
