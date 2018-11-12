a = input()
str_ = input()

str_list = list(str_)
list_ = []

for i in range(0, int(a)-1):
    temp = list(str_)
    del temp[i]
    list_.append(''.join(temp))

print(min(list_))
