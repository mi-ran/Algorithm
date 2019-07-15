a = int(input())
str_ = input()

str_list = list(str_)

for i in range(0, a-1):
    if str_list[i] > str_list[i + 1]:
        del str_list[i]
        break

if len(str_list) < a:
    print(''.join(str_list))
else:
    print(''.join(str_list[0:-1]))
