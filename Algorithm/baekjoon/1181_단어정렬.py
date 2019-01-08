N = int(input())

li_word = []

for i in range(N):
    msg = input()
    li_word.append(msg)

li_word = list(set(li_word))
li_word.sort()
new_li = sorted(li_word, key=len)

for nl in new_li:
    print(nl)