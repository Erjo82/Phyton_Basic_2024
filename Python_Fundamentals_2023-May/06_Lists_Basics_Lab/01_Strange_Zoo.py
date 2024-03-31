head = input()
body = input()
tail = input()
meerkat_list = [head, body, tail]
meerkat_list[0], meerkat_list[2] = meerkat_list[2], meerkat_list[0]
print(meerkat_list)
