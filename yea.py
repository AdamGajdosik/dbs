import os

for root, dirs, files in os.walk('mydata'):

     for file in files:
        with open(os.path.join(root, file), "r") as auto:
            try:
                for line in auto.readlines():
                    print(line)
            except:
                continue