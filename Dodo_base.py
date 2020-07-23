import json
from random import choice

"""
--Availabel Instructions---
i) dodo
ii) how are you
iii) what are  you doing
iv) whats up
"""

db = json.load(open("database/Instructions.json"))
print("\t\t----Program Started----")
flag = False

while 1:
    check = input("<< ")

    for i in db:
        if check in i:
            print(">> " + db[i][db[i].index(choice(db[i]))])
            flag = True
            break
        else:
            flag = False

    if not flag:
        print(">> NO results")
# -------------------------------------------
