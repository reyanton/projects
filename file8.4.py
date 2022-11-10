fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
for line in fh:
    lst =  lst + line.split()

for i in range(len(lst)):
    if lst[i] in words: continue
    words.append (lst[i])

words.sort()
print(words)
