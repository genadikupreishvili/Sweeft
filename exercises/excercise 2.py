

def biggerIsGreater(w):
    # i start from the second-last character because i need to compare each character with the character to its right
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1

    #  it means that the input string is already the largest lexicographically possible
    if i < 0:
        return "no answer"


    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    w = list(w)
    w[i], w[j] = w[j], w[i]

    # i need to rearrange the characters
    w[i+1:] = reversed(w[i+1:])

    # i need to convert the list w back to a string
    return "".join(w)

t = int(input("input number of test cases:   :"))
for i in range(t):
    w = input("input word;))  :").strip()
    print(biggerIsGreater(w))
