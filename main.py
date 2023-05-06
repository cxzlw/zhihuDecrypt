from utils import *

c = get_cdycc(5396)
print("got")
print(detect_encrypt_method_with_probability(c))
print(decrypt(c, detect_encrypt_method(c)))
