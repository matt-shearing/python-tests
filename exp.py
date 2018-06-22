import re

l = "Beautiful is better than ugly."
zen = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

string = "Two too."

string2 = "123?hi 34 hello?"

k = re.findall("t[wo]o",
               string,
               re.IGNORECASE)

a = re.findall("\d",
               string2,
               re.IGNORECASE)

t = "__one__ __two__ __three__"

matches = re.findall("beautiful", l, re.IGNORECASE)

m = re.findall("^If", zen, re.MULTILINE)

found = re.findall("__.*?__", t)

for match in found:
    print(match)

print(m)
print(k)
print(matches)
print(a)