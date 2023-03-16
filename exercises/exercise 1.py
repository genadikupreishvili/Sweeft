#n = number of words
n = int(input("Input number of words :"))
words = []
for i in range(n):
    words.append(input("Input word :").strip())

# I created a dictionary to identify how many times a word is repeated.
word_count = {}
for i in words:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] +=1

# I print the number of distinct word:
print(len(word_count))

# count of each distinct word:
for i in word_count.values():
    print(i, end = " ")