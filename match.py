import re

z = "The ghost that says boo haunts the loo"

x = re.findall(".oo", z)

print(x)