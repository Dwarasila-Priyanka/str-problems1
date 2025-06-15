#1. Print a specific part of a string without using slicing
text="priyanka"
res=""
for i in range(2,6):
    res+=text[i]
    print(res) #iyan


# 2. Print the string to replace "is" with "si" without using replace method
a = "hi this is ram and is raj"
words = a.split()
new_words = []

for i in words:
    if i == "is":
        new_words.append("si")
    else:
        new_words.append(i)

res = " ".join(new_words)
print(res) #hi this si ram and si raj


