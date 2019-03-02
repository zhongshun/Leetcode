s = "pwwkew"
cur = 0
Longest = 0
seen = {}
list = []
for index, letter in enumerate(s):
    if letter not in list:
        list.append(letter)
    else:
        list = list[list.index(letter)+1:]
        list.append(letter)
    Longest = max(Longest, len(list))

print(Longest)
