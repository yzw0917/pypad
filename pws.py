import itertools as s
words="1234567890abc"
r=s.product(words,repeat=6)
# for i in r:
#     print(i)
file=open("passwd.txt","a")
for i in r:
    file.write("".join(i))
    file.write("".join("\n"))