# s = "jj gg hh"
# s_list = s.split(" ")
# print(s_list)
# ss = s_list[0] + s_list[1]
# print(type(s))
# print(type(s_list))
# print(type(ss))
import re

t = []
t[0] = "oiiiiiii\n"
t[1] = "doisssss\n"
q = str(t)
tt = re.sub(r'[\n]', '', q)
print(tt)