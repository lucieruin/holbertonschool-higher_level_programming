#!/usr/bin/python3
alpha = ""
for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        alpha += chr(i)
print("{}".format(alpha), end="")
