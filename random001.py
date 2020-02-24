import random

r_ip=["192.168.10.63",
      "20.15.25.142",
      "30.123.53.35",
      "987.123.324.556"]

for i in range(1,100):
      print(random.choice(r_ip))
      print(random.randint(1,10000))
